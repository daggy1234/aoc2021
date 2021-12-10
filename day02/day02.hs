{-# OPTIONS_GHC -Wno-incomplete-patterns #-}
module Main where

main :: IO ()

data Instruction = Instruction {instructionAction :: String, instructionValue::  Int}

instructionParserLine :: String ->  Instruction
instructionParserLine line = Instruction (head (words line)) (read (words line !! 1) :: Int)

instructionParser :: String ->  [Instruction]
instructionParser inp = map instructionParserLine $ lines inp


applyStepPartA :: [Instruction] -> Int -> Int -> Int
applyStepPartA instructions dir dep = prod
    where
        prod = if null instructions
               then dir * dep
               else 
                case instructionAction (head instructions) of 
                    "forward" -> applyStepPartA (drop 1 instructions) (dir + instructionValue (head instructions)) dep
                    "up" -> applyStepPartA (drop 1 instructions) dir (dep - instructionValue (head instructions))
                    "down" -> applyStepPartA (drop 1 instructions) dir (dep + instructionValue (head instructions))

applyStepPartB :: [Instruction] -> Int -> Int -> Int -> Int
applyStepPartB instructions dir dep aim = prod
    where
        prod = if null instructions
               then dir * dep
               else 
                case instructionAction (head instructions) of 
                    "forward" -> applyStepPartB (drop 1 instructions) (dir + instructionValue (head instructions)) (dep + (aim * instructionValue (head instructions))) aim
                    "up" -> applyStepPartB (drop 1 instructions) dir dep (aim - instructionValue (head instructions)) 
                    "down" -> applyStepPartB (drop 1 instructions) dir dep (aim + instructionValue (head instructions))


main = do 
    parta <- readFile "data.txt"
    let parsedList = instructionParser parta
    let out_a = applyStepPartA parsedList 0 0
    print "Part 1:"
    print out_a
    let out_b = applyStepPartB parsedList 0 0 0
    print "Part 2:"
    print out_b