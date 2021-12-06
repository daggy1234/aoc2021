module Main where

main :: IO ()

intListParser :: String ->  [Int]
intListParser inp = map read $ words inp

questionA :: [Int] -> Int -> Int -> Int
questionA numList minval count = nr
    where
        nr = if null numList
             then count
             else questionA (drop 1 numList) (head numList) (count + if head numList > minval then 1 else 0)


questionB :: [Int] -> Int -> Int -> Int
questionB numList minval count = nr
    where
        lSum = head numList + numList !! 1 + numList !! 2
        nr = if length numList == 2
             then count
             else questionB (drop 1 numList) lSum (count + if lSum > minval then 1 else 0)

main = do 
    parta <- readFile "data.txt"
    let intList = intListParser parta
    let out_d1 = questionA (drop 1 intList) (head intList) 0
    print out_d1
    let out_d2 = questionB (drop 1 intList) (head intList + intList !! 1 + intList !! 2) 0
    print out_d2