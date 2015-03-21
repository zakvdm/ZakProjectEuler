module Solutions.Problem77 where
{-
The idea is to just modify 76 as needed
-}
import Data.List
import qualified Data.Set as Set
import qualified Data.Map as Map
import Data.Numbers.Primes

range :: Int
range = 80

run :: IO ()
run = print $ map prettyPrint (Map.elems (solution range))

prettyPrint :: Value -> String
prettyPrint v = "x: " ++ show (x v) ++ ", count: " ++ show (count v)
{-
 - x -> The actual value
 - count -> The number of ways to sum primes to make x
 - ways -> A map of the number of ways to make x where the key is the minimum size of
           the primes used
 -}
data Value = Value { x :: Int, count :: Int, ways :: Map.Map Int Int } deriving (Show, Eq)

emptyValue :: Value
emptyValue = Value { x = 1, count = 0, ways = Map.empty }

start :: Map.Map Int Value
start = Map.fromList [(1,emptyValue)]

{-
 - primesBetween 7 29 == [11,13,17,19,23,29]
 -}
primesBetween :: Int -> Int -> [Int]
primesBetween min max = takeWhile (<= max) $ dropWhile (< min) primes

-- For the given n, work out the number of sums that 
-- produce n and only include terms of minimum size min
-- min > 2
-- n > 4
-- lhs > 2
-- primesBetween 2 4 = [2, 3]
-- 
lkup :: Map.Map Int Value -> Int -> Int -> Int
lkup m n min =
    let lhs = (n - min) -- i.e. lhs + min == n
        ws = ways (m Map.! lhs)
        primeSums y | Map.member y ws = ws Map.! y
                    | isPrime y && y == lhs = 1
                    | otherwise = 0
        -- NOTE: Is it necessary to use primesBetween here?
        waysToMake = sum (map primeSums (primesBetween min lhs))
    in waysToMake


step :: Map.Map Int Value -> Int -> Map.Map Int Value
step m x = let max = floor ((fromIntegral x) / 2)
               r = takeWhile (<=max) primes
               build y = (y, lkup m x y)
               ws = map build r
               c = sum (map snd ws)
               v = Value { x = x, count = c, ways = (Map.fromList ws) }
           in Map.insert x v m  

solution :: Int ->  Map.Map Int Value
solution n = foldl step start [2..n]
