module Main where

main :: IO ()

main = do 
    parta <- readFile "test_data.txt"
    let intList = lines parta
    print (head intList)
    print (countCharsMaxMin  (head intList))


countCharsMaxMin :: String -> (String,String )
countCharsMaxMin inp = a
    where
         lv = length inp
         oc = countChars inp 0
         zc = lv - oc
         a = if zc > oc then ("0", "1") else ("1", "0")


countChars :: String -> Int  -> Int
countChars inp oc = foc 
        where
            foc = if null inp
                 then oc
                 else countChars (drop 1 inp) (oc + if head inp == '1' then 1 else 0)
