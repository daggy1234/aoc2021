import GHC.IO (unsafePerformIO)
import Debug.Trace (traceIO)

main :: IO ()


trace :: String -> a -> a
trace str expr = unsafePerformIO $ do
    traceIO str
    return expr

main = do
    let out = trace "will be trace" 10
    print out