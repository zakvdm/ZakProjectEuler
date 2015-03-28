module Solutions.Problem81 where
{-
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
-}

import Data.Ord
import Prelude as P
import qualified Data.List as L
import qualified Data.Map as M
import qualified Data.Set as S

run :: IO ()
run = print "hello"

data Node = Node Int Int deriving (Eq, Ord, Show)

-- TODO: Size can be part of State instead of here and in costs?
data Matrix a = Matrix (M.Map Node a) deriving Show

data Cost = Cost Int | Unknown deriving (Eq, Ord, Show)

data State = State { size :: Int, values :: Matrix Int, costs :: Matrix Cost, visited :: S.Set Node } deriving Show

findPath :: State -> Node -> State
findPath s@(State { visited = vs }) target
    | (S.member target vs) = s
    | otherwise = findPath (step s) target

step :: State -> State
step (State { size = s, values = vs, costs = cs, visited = vsted }) =
    let node = nextNode cs vsted
        cost = getCost cs node
        ngbrs = neighbours s node
        newCosts = updateNeighbours vs cs cost ngbrs
        newVisited = S.insert node vsted
    in State { size = s, values = vs, costs = newCosts, visited = newVisited }

initialState :: State
initialState = State { size = 5, values = example, costs = initialCosts, visited = S.empty }

initialCosts :: Matrix Cost
initialCosts = Matrix $ M.fromList [(Node 0 0, Cost (getValue example (Node 0 0)))]

example :: Matrix Int
example = let row x columns = L.map (Node x) [0..columns]
          in Matrix $ M.fromList $
               zip (row 0 4) [131, 673, 234, 103, 18] 
            ++ zip (row 1 4) [201, 96, 342, 965, 150] 
            ++ zip (row 2 4) [630, 803, 746, 422, 111] 
            ++ zip (row 3 4) [537, 699, 497, 121, 956] 
            ++ zip (row 4 4) [805, 732, 524, 37, 331] 

getValue :: Matrix Int -> Node -> Int
getValue (Matrix vs) n = M.findWithDefault (error "Why?") n vs

getCost :: Matrix Cost -> Node -> Cost
getCost (Matrix cs) n = M.findWithDefault Unknown n cs

addCost :: Matrix Cost -> Node -> Cost -> Matrix Cost
addCost (Matrix cs) n c = Matrix $ M.insert n c cs

neighbours :: Int -> Node -> [Node]
neighbours size' (Node x y) =
    let n = [Node x (y+1), Node (x+1) y]
    in filter (\(Node a b) -> a < size' && b < size') n

updateNeighbours :: Matrix Int -> Matrix Cost -> Cost -> [Node] -> Matrix Cost
updateNeighbours _ _ Unknown _ = error "Ancestor cost can't be unknown"
updateNeighbours _ cs _ [] = cs
updateNeighbours vs cs (Cost c) ns =
    let newCost :: Node -> Int
        newCost node = c + getValue vs node
        bestCost :: Matrix Cost -> Node -> Cost
        bestCost cs' node = Cost $ case getCost cs' node of
            Unknown -> c + (getValue vs node)
            Cost old -> min old (newCost node)
        updateNeighbour :: Matrix Cost -> Node -> Matrix Cost
        updateNeighbour cs' node = addCost cs' node (bestCost cs' node) 
    in foldl updateNeighbour cs ns

-- Find the Node with the lowest cost that has not yet been visited
-- NOTE: Cost 1000000 < Unknown
nextNode :: Matrix Cost -> S.Set Node -> Node
nextNode (Matrix cs) vs =
    let keys = L.filter (\n -> not (S.member n vs)) (M.keys cs)
    in L.minimumBy (comparing (\k -> cs M.! k)) keys

          
