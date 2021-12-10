module Main where
import Data.Map (Map)
import qualified Data.Map as Map
import Data.Set (Set)
import Data.List
import qualified Data.Set as Set
import qualified GHC.Generics as Map
import Data.Maybe

main :: IO ()


data InpNum = InpNum {input :: Maybe String, value::  Int}

processLines :: String -> [String]
processLines = lines

processInp :: String -> [Char] -> [Char]
processInp inp stack = foldl (\ stack x -> stack ++ [x]) stack inp

pop :: [a] -> [a]
pop [] = []
pop xs = init xs

removeItem _ []                 = []
removeItem x (y:ys) | x == y    = removeItem x ys
                    | otherwise = y : removeItem x ys

purgeStack :: Char -> [Char] -> [Char]
purgeStack inp stack = if last stack == inp then pop stack else purgeStack inp (pop stack)

runWithStack :: [Char] -> [Char] -> Map Char Char  -> [Char]  -> [Char] -> [Char]
runWithStack [] toCheck sets stack empt = empt
runWithStack (y:ys) toCheck sets stack empt | y `elem` toCheck = runWithStack ys toCheck sets (stack ++ [y]) empt
                                            | y == (sets Map.! last stack) = runWithStack ys toCheck sets (pop stack) empt
                                            | otherwise = runWithStack ys toCheck sets (pop stack) (empt ++ [y])


filterWithStack :: [Char] -> [Char] -> Map Char Char  -> [Char]  -> [Char]
filterWithStack [] toCheck sets stack = stack
filterWithStack (y:ys) toCheck sets stack | y `elem` toCheck = filterWithStack ys toCheck sets (stack ++ [y])
                                          | otherwise = filterWithStack ys toCheck sets (purgeStack (sets Map.! y) stack)



processEachLine :: String -> InpNum
processEachLine inp = InpNum (if length out == 1 then Nothing else Just inp ) (if length out == 1 then Map.fromList [(')',3),(']', 57), ('}', 1197), ('>', 25137)] Map.! head out else 0)
    where
        out = runWithStack (processInp inp []) ['[', '(', '{', '<'] (Map.fromList [('(', ')'), (')', '('), ('[', ']'), (']', '['), ('{', '}'), ('}', '{'), ('<', '>'), ('>', '<')]) [] []

processEachLineFilter :: String -> String
processEachLineFilter inp = fromMaybe "" (input p)
    where
        p = processEachLine inp



scoreCompletions :: [Char] -> Map Char Char -> Map Char Int  ->  Int -> Int
scoreCompletions [] sets scores t = t
scoreCompletions (x: xs) sets scores t = scoreCompletions xs sets scores ((t * 5) + scores Map.! (sets Map.! x))

processEachLinePt2 :: String -> Int
processEachLinePt2 inp = scoreCompletions (reverse (filterWithStack (processInp inp []) ['[', '(', '{', '<'] (Map.fromList [('(', ')'), (')', '('), ('[', ']'), (']', '['), ('{', '}'), ('}', '{'), ('<', '>'), ('>', '<')]) [])) (Map.fromList [('(', ')'), (')', '('), ('[', ']'), (']', '['), ('{', '}'), ('}', '{'), ('<', '>'), ('>', '<')]) (Map.fromList [(')',1),(']',2),('}',3),('>',4)]) 0

part1 :: [String] -> Int
part1 inp = sum (map (value .processEachLine) inp)

part2 :: [String] -> Int
part2 inp = oval !! (length oval `div` 2)
    where
        oval = sort (map  processEachLinePt2  (removeItem "" (map processEachLineFilter inp)))

main = do
    parta <- readFile "test_data.txt"
    let line_parsed = processLines parta
    print "Part 1:"
    print (part1 line_parsed)
    print "Part 2:"
    print (part2 line_parsed)
