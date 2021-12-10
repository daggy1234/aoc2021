module Main where
import Data.Map (Map)
import qualified Data.Map as Map
import Data.Set (Set)
import Data.List
import qualified Data.Set as Set
import qualified GHC.Generics as Map
import GHC.IO (unsafePerformIO)
import Debug.Trace (traceIO)


main :: IO ()

trace :: String -> a -> a
trace str expr = unsafePerformIO $ do
    traceIO str
    return expr

data InpNum = InpNum {input :: String, value::  Int}

processLines :: String -> [String]
processLines = lines

processInp :: String -> [[Char]] -> [[Char]]
processInp inp stack = if null inp then stack else processInp (drop 1 inp) (stack ++ [[head inp]])

pop :: [a] -> [a]
pop [] = []
pop xs = init xs

removeItem _ []                 = []
removeItem x (y:ys) | x == y    = removeItem x ys
                    | otherwise = y : removeItem x ys

purgeStack :: String -> [[Char]] -> [[Char]]
purgeStack inp stack = 
    if last stack == inp
        then pop stack 
    else 
        purgeStack inp (pop stack)

runWithStack :: [[Char]] -> [[Char]] -> Map String String  -> [[Char]]  -> [[Char]] -> [[Char]]
runWithStack [] toCheck sets stack empt = empt
runWithStack (y:ys) toCheck sets stack empt = vals
    where
        vals
            | y == "" = runWithStack ys toCheck sets stack empt
            | y `elem` toCheck = runWithStack ys toCheck sets (stack ++ [y]) empt
            | y == (sets Map.! last stack) = runWithStack ys toCheck sets (pop stack) empt
            | otherwise = runWithStack ys toCheck sets (pop stack) (empt ++ [y])


filterWithStack :: [[Char]] -> [[Char]] -> Map String String  -> [[Char]]  -> [[Char]]
filterWithStack [] toCheck sets stack = stack
filterWithStack (y:ys) toCheck sets stack = vals
    where
        vals
            | y == "" = filterWithStack ys toCheck sets stack
            | y `elem` toCheck = filterWithStack ys toCheck sets (stack ++ [y])
            | otherwise = filterWithStack ys toCheck sets (purgeStack (sets Map.! y) stack)



processEachLine :: String -> InpNum
processEachLine inp = InpNum inp outv
    where
        out = removeItem "" (runWithStack (processInp inp [[]]) ["[", "(", "{", "<"] (Map.fromList [("(", ")"), (")", "("), ("[", "]"), ("]", "["), ("{", "}"), ("}", "{"), ("<", ">"), (">", "<")]) [[]] [[]])
        outv = if length out == 1 then Map.fromList [(")",3),("]", 57), ("}", 1197), (">", 25137)] Map.! head out  else 0

processEachLineFilter :: String -> String
processEachLineFilter inp = outv
    where
        p = processEachLine inp
        outv = if value p == 0 then input p else ""



scoreCompletions :: [[Char]] -> Map String String -> Map String Int  ->  Int -> Int
scoreCompletions [] sets scores t = t
scoreCompletions (x: xs) sets scores t = outs
    where
        outs = scoreCompletions xs sets scores ((t * 5) + scores Map.! (sets Map.! x))

processEachLinePt2 :: String -> Int
processEachLinePt2 inp = scoreCompletions (reverse (removeItem "" (filterWithStack (processInp inp [[]]) ["[", "(", "{", "<"] (Map.fromList [("(", ")"), (")", "("), ("[", "]"), ("]", "["), ("{", "}"), ("}", "{"), ("<", ">"), (">", "<")]) [[]]))) (Map.fromList [("(", ")"), (")", "("), ("[", "]"), ("]", "["), ("{", "}"), ("}", "{"), ("<", ">"), (">", "<")]) (Map.fromList [(")",1),("]",2),("}",3),(">",4)]) 0

part1 :: [String] -> Int
part1 inp = sum (map (value .processEachLine) inp)

part2 :: [String] -> Int
part2 inp = outval
    where
        somev = removeItem "" (map processEachLineFilter inp)
        oval = sort (map  processEachLinePt2  somev)
        outval = oval !! (length oval `div` 2)

main = do
    parta <- readFile "data.txt"
    let line_parsed = processLines parta
    print "Part 1:"
    print (part1 line_parsed)
    print "Part 2:"
    print (part2 line_parsed)
