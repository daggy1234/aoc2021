module Main where
import Data.Text (splitOn, Text, unpack, singleton, pack)

main :: IO ()

splitCommaString :: String -> [Int]
splitCommaString inp = map (read . unpack) (splitOn (singleton ',') (pack inp))


computeSimpleFuelForVal ::  [Int] -> Int -> Int
computeSimpleFuelForVal inp pos = sum [abs (pos - i)|i <- inp]

computeComplexFuelForVal :: [Int] -> Int -> Int
computeComplexFuelForVal inp pos = sum [sum [0..(abs (pos - i))]|i <- inp]

part1 :: [Int] -> Int
part1 parsed = minimum (map (computeSimpleFuelForVal parsed) [(minimum parsed)..(maximum parsed)])
-- part1 parsed = minimum [computeSimpleFuelForVal c parsed |c <- [(minimum parsed)..(maximum parsed)]]


part2 :: [Int] -> Int
part2 parsed = minimum (map (computeComplexFuelForVal parsed) [(minimum parsed)..(maximum parsed)])
-- part2 parsed = minimum [computeComplexFuelForVal parsed c |c <- [(minimum parsed)..(maximum parsed)]]

main = do 
    parta <- readFile "data.txt"
    let parsed = splitCommaString parta
    print (part1 parsed)
    print (part2 parsed)