def factorial(n):
  if(n==1 or n==0):
    return 1
  else:
    return(n*factorial(n-1))
num=5;
print("Enter a number:",num)
print("The factorial of a number is:",factorial(num))