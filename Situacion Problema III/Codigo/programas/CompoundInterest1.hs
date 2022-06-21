compoundInterest :: Int -> Double 
compoundInterest 0 = 1000 
compoundInterest n = 1.05 * (compoundInterest (n - 1))  
main = printf "After 10 years, you have %.2f dollars." (compoundInterest 10) 