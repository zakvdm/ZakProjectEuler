module Solutions.Problem76 where
{-
The basic idea behind this algorithm is this:

For any number n, the total number of sums is:
a) The number of sums that have at least one 1 in them
b) + The number of sums that have at least one 2 in them (but no 1s otherwise we double count)
c) + So on until we get to (floor (n / 2)) since we don't want to double count

Now, the next trick is realising that in (a) (b) & (c) above, you can calculate the value
by adding 1 to the previous values (appropriate looked up in the history)

This makes the algorithm roughly O(n^2), I think. Not great, but good enough for n=100
-}
import Data.List
import qualified Data.Set as Set
import qualified Data.Map as Map

target :: Int
target = 100

run :: IO ()
run = print $ solution target

data Value = Value { x :: Int, count :: Int, ways :: Map.Map Int Int } deriving (Show, Eq)

getWays :: Value -> Map.Map Int Int
getWays = ways

emptyValue :: Value
emptyValue = Value { x = 1, count = 0, ways = Map.empty }

start :: Map.Map Int Value
start = Map.fromList [(1,emptyValue)]

-- For the given max (effectively n), work out the number of sums that 
-- produce max and only include terms of minimum size y
lkup :: Map.Map Int Value -> Int -> Int -> Int
lkup m max y =
    let lhs = (max - y)
        ws = ways (m Map.! lhs)
    in sum (map (\z -> Map.findWithDefault 0 z ws) [y..max])


step :: Map.Map Int Value -> Int -> Map.Map Int Value
step m x = let max = floor ((fromIntegral x) / 2)
               r = [1..max]
               build y = (y, 1 + (lkup m x y))
               ws = map build r
               c = sum (map snd ws)
               v = Value { x = x, count = c, ways = (Map.fromList ws) }
           in Map.insert x v m  

solution :: Int -> Value
solution n = (foldl step start [2..n]) Map.! n
