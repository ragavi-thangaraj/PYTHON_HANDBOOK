# Syntax: 
#          value_if_true  if_condition  else  value_if_false

a = int(input("A : "))       
b = int(input("B : "))        

# Using ternary operator to find the greater number
result = "A is greater than B" if a > b else "B is greater than A"

print(result)

# Sample Output:
# A : 10
# B : 7
# A is greater than B
