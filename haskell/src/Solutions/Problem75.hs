module Solutions.Problem75 where
  {- The basic approach is as follows:
     * Generate all primitive pythagorean triples using https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
     * All primitive triples go in a set so there's only one of each
     * Iterate through set and increment count of every multiple of the length <= 1500000 (use a Map for this)
     * The result is a count of keys in the map with a value 1
  -}
import Primes
import Data.List
import qualified Data.Set as Set
import qualified Data.Map as Map

run :: IO ()
--run = print (Set.size primitiveTriples)
run = print (Map.size (Map.filter (==1) triplesMap))
--run = print (Map.fold (+) 0 triplesMap)

data Triple = Triple Int Int Int deriving (Eq, Ord, Show)

tripleLength :: Triple -> Int
tripleLength (Triple a b c) = a + b + c

-- m < n - https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
toTriple :: Int -> Int -> Triple
toTriple m n = let m' = m * m
                   n' = n * n
                   a = m' - n'
                   b = 2 * m * n
                   c = m' + n'
               in if a < b then Triple a b c else Triple b a c

maxL :: Int
maxL = 1500000
-- This is an upper bound since c^2 = m^2 + n^2 (where m & n > 0)
maxM :: Int
maxM = (round . sqrt . fromIntegral) maxL

primitiveTriples :: Set.Set Triple
primitiveTriples = Set.fromList (primitiveTriples' [2..maxM])

primitiveTriples' :: [Int] -> [Triple]
primitiveTriples' [] = []
primitiveTriples' (m:ms) = (findTriples m) ++ primitiveTriples' ms

findTriples :: Int -> [Triple]
findTriples m = let validN n = (odd (m - n)) && coprime m n
                    ns = filter validN [1..(m-1)]
                    ts = map (toTriple m) ns
                in filter (\t -> maxL >= tripleLength t) ts

takeTriple :: Map.Map Int Int -> Triple -> Map.Map Int Int
takeTriple m t = let l = tripleLength t
                     ls = takeWhile (< maxL) [l,(2*l)..]
                 in foldl takeLength m ls

takeLength :: Map.Map Int Int -> Int -> Map.Map Int Int
takeLength m l = Map.insertWith (+) l 1 m

triplesMap :: Map.Map Int Int
triplesMap = foldl takeTriple Map.empty (Set.toList primitiveTriples)
