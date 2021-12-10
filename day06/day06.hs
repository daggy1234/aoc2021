module Main where

main :: IO ()

-- From Stackoverflow but I actually understood
splitCommaString :: String -> [Int]
splitCommaString inp = map read $ words [if c == ',' then ' ' else c|c <- inp]

subFromAll :: [Int] -> [Int]
subFromAll = map (subtract 1)

countOccur :: [Int] -> Int -> Int
countOccur inp toC = sum [if c == toC then 1 else 0|c <- inp]

remove :: Int -> [Int] -> [Int]
remove element = filter (/=element)

tickTimer :: [Int] -> [Int]
tickTimer inp = out
    where
        sub = subFromAll inp
        noCount = countOccur sub (-1)
        renOut = if noCount == 0 then sub else sub ++ replicate noCount 8 ++ replicate noCount 6
        out = remove (-1) renOut

part1 :: Int -> [Int] -> Int
part1 recur inp = if recur == 0 then length inp else part1 (recur - 1) (tickTimer inp)

initialOccurHack :: Int -> Int  -> [Int] -> [Int] -> [Int]
initialOccurHack maxS ct inp par = if ct == maxS then inp else initialOccurHack maxS (ct + 1) (inp ++ [countOccur par ct]) par

tickTimerEff :: [Int] -> [Int]
tickTimerEff inp = [inp !! 1, inp !! 2, inp !! 3, inp !! 4, inp !! 5, inp !! 6, inp !! 7 + head inp, inp !! 8, head inp]

-- tickTimerEff :: [Int] -> [Int]
-- tickTimerEff inp = take 5 (drop 1 inp) ++ [inp !! 6 + head inp] ++ take 2 (drop 7 inp) ++ [head inp]

part2 :: Int -> [Int] -> Int
part2 recur inp = if recur == 0 then sum inp else part2 (recur - 1) (tickTimerEff inp)

main = do 
    parta <- readFile "data.txt"
    let parsed = splitCommaString parta
    print "Part 1:"
    print (part1 80 parsed)
    print "Part 2:"
    print (part2 256 (initialOccurHack 9 0 [] parsed))