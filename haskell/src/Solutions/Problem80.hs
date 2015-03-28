module Solutions.Problem80 where
{-
This is a hacky solution which uses CReal types and lots of String parsing...
-}

import Data.Char
import Data.Number.CReal

run :: IO ()
run = print sums

roots :: [String]
roots = let realRoots = map sqrt [1..100 :: CReal]
        in map (showCReal 150) realRoots

irrationalRoots :: [String]
irrationalRoots = let isInteger x = ".0" == dropWhile (/= '.') x
                      irs = filter (not . isInteger) roots
                      irs' = map (filter (/= '.')) irs
                  in map (take 100) irs'

sums :: Int
sums = let toSum :: String -> Int
           toSum root = sum $ map digitToInt root
           allSums = map toSum irrationalRoots
       in sum allSums

