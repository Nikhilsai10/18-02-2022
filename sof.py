def factorial(n):
    if n==1:
        return n
    elif n==0:
        return 1
    else:
        return n*factorial(n-1)
    
Num=input("Enter the value:")
sum=0
for ele in Num:
      sum+=factorial(int(ele))
      print(sum)
