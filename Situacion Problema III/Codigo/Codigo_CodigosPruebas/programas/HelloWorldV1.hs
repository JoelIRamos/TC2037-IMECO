main :: IO () 
main = do 
   putStrLn "Hello! What's your name?" 
   name <- getLine 
   let statement = helloPerson name 
   putStrLn statement 