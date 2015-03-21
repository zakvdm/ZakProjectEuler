module Solutions.Problem79 where
{-
The trick here is to realise that if every candidate you construct is a valid
solution along the way, then you can always only keep the shortest ones. This
is because you can always add in additional characters later.
-}

import Data.List
import Data.Function (on)

run :: IO ()
run = print solutions

pins :: [String]
pins = map show $ nub
  [ 319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 368, 710, 720,
    710, 629, 168, 160, 689, 716, 731, 736, 729, 316, 729, 729, 710,
    769, 290, 719, 680, 318, 389, 162, 289, 162, 718, 729, 319, 790,
    680, 890, 362, 319, 760, 316, 729, 380, 319, 728, 716
  ]

data Solution = Solution String [String] deriving Show

solutions :: [Solution]
solutions = scanl step (Solution (head pins) [head pins]) (tail pins)

step :: Solution -> String -> Solution
step (Solution _ []) next = Solution next [next]
step (Solution _ xs) next = let all = concat $ map (mix next) xs
                                squashed = map squash all
                                candidates = takeShortest squashed
                            in Solution next (nub candidates)

-- mix "de" "abc" => ["deabc","daebc","dabec","dabce","adebc","adbec","adbce","abdec","abdce","abcde"]
mix :: String -> String -> [String]
mix "" s = [s]
mix [x] s = zipWith (\lhs rhs -> lhs ++ (x : rhs)) (inits s) (tails s)
mix (x:xs) s = let f lhs rhs = map ((lhs ++ [x]) ++) (mix xs rhs)
               in concat $ zipWith f (inits s) (tails s)

-- squash "abbbcbbdd" => "abcbd"
squash :: String -> String
squash "" = ""
squash (x:xs) = x : squash (dropWhile (== x) xs)

-- takeShortest ["abc","ab","defg","aa"] => ["ab", "aa"]
takeShortest :: [String] -> [String]
takeShortest xs = let sorted = sortBy (compare `on` length) xs
                      isShortest xs = (length xs) == (length (head sorted))
                  in takeWhile isShortest sorted

