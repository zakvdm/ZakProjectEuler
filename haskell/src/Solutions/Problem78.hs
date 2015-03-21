module Solutions.Problem78 where
{-

-}
import Control.Applicative
import Data.List
import qualified Data.Set as Set
import qualified Data.Map as Map

run :: IO ()
--run = print $ find (\x -> x `mod` 100000 == 0) (map p [1..])
run = print $ find (\(k,v) -> v `mod` 1000000 == 0) (Map.toList (foldl p'' Map.empty [1..100000]))
--run = print $ find (\x -> x `mod` 100000 == 0) (map p [1..])

lkup :: Map.Map Integer Integer -> Integer -> Integer
lkup m term
    | term == 0 = 1
    | term < 0 = 0
    | otherwise = m Map.! term

p'' :: Map.Map Integer Integer -> Integer -> Map.Map Integer Integer
p'' m n = let left k = lkup m (leftTerm' n k)
              right k = lkup m (rightTerm' n k)
              f k = (prefix k) * ((left k) + (right k))
              s = sum $ map f [1..n]
          in Map.insert n s m
                  




prefix :: Integer -> Integer
prefix k = floor $ (-1) ** ((fromIntegral k) + 1)

moderator :: Fractional a => Integer -> Integer -> a
moderator x k = fromIntegral $ k * ((3*k) + x)

leftTerm' :: Integer -> Integer -> Integer
leftTerm' n k = n - (floor ((moderator (-1) k) / 2))

rightTerm' :: Integer -> Integer -> Integer
rightTerm' n k = n - (floor ((moderator 1 k) / 2))

