num=int(input("Enter a number : "))
sum=0
val=num 
while num:
    rem=num%10
    sum+=rem
    num=num//10
print(f"The sum of digits of {val} is {sum}")

# Sample output
# Enter a number : 333
# The sum of digits of 333 is 9