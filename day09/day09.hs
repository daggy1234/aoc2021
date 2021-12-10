module Main where


main :: IO ()


parseInp :: String -> [[Int]]
parseInp inp = map (read words) $ (lines inp)


main = do
    parta <- readFile "test_data_b.txt"
    print parta
    -- let parsed = parseInp parta
    -- print parsed
