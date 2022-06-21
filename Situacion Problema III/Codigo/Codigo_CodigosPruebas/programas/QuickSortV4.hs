-- Using list comprehensions 
quickSort []     = []                               -- The empty list is already sorted 
quickSort (x :: xs) = quickSort [a | a <- xs, a < x]   -- Sort the left part of the list 
                   ++ [x] ++                        -- Insert pivot between two sorted parts 
                   quickSort [a | a <- xs, a >= x]  -- Sort the right part of the list 