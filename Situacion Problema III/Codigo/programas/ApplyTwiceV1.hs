applyTwice :: (Int -> Int) -> Int -> Int 
applyTwice f x = f (f x) 
double :: Int -> Int 
double x = 2 * x 
next :: Int -> Int 
next x = x + 1 
main = do 
  print (applyTwice double 2) -- quadruples 
  print (applyTwice next 1) --adds 2 