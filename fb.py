def fib(n):
   
   if n <= 1:
       return n
   else:
       return(fib(n-1) + fib(n-2))

nterms = 10

if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(fib(i))
