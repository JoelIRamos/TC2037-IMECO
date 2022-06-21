applyTwice :: (Int -> Int) -> Int -> Int 
applyTwice f = f . f 
main = do  
  print (applyTwice (\x -> x * 2) 8) 
  print (applyTwice (\x -> x + 1) 7) 