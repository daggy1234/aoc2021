module Main where
import Data.Text (splitOn, Text, unpack, singleton, pack)
import Data.Map (Map)
import qualified Data.Map as Map
import Data.Set (Set)
import qualified Data.Set as Set


main :: IO ()

parseInpLine :: String -> [[String]]
parseInpLine inp = map (words . unpack) (splitOn (singleton '|') (pack inp))



parseInp :: String -> [[[String]]]
parseInp inp = map parseInpLine $ lines inp

checkIfStandard :: String -> Int
checkIfStandard inp = if length inp `elem` [2,4,7,3] then 1 else 0

part1 :: [[[String]]] -> Int
part1 inp = sum [sum (map checkIfStandard (last subinp)) | subinp <- inp]

makeDict :: Map Int Int
makeDict = Map.fromList [(2,1),(4,4),(3,7),(7,8)]

makeSetMap :: [String] -> Map Int Int ->  Map Int (Set Char) -> Map Int [Set Char] -> Bool
makeSetMap inp mapping sorted new = out
    where
        e = [if length val `elem` [2,4,7,3] then Map.insert (mapping Map.! length val) (Set.fromList val) sorted  else Map.insert (length val) (Set.fromList val) sorted |val <- inp ]
        out = True

main = do
    parta <- readFile "test_data.txt"
    let parsed = parseInp parta
    let sorted_map = Map.empty
    let o = makeSetMap (head (head parsed)) makeDict sorted_map Map.empty
    print o
