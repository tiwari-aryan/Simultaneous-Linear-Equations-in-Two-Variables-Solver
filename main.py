import re


print("This python program will solve any Simultaneous Linear Equation \n")
fe = (input("First Equation: "))
se = (input("Second Equation: "))

# write the regular expression to obtain the coefficient of the x, y & = b

x1 = re.findall("[0-9]*.[0-9]*x", fe)
y1 = re.findall("[0-9]*.[0-9]*y", fe)
b1 = re.findall("=[0-9]*.[0-9]*", fe)

x2 = re.findall("[0-9]*.[0-9]*x", se)
y2 = re.findall("[0-9]*.[0-9]*y", se)
b2 = re.findall("=[0-9]*.[0-9]*", se)

# code if x or y is written without a coeffiecient

x1 = float(x1[0][:-1])
x2 = float(x2[0][:-1])
y1 = float(y1[0][:-1])
y2 = float(y2[0][:-1])
b1 = float(b1[0][1:])
b2 = float(b2[0][1:])

# main final code
# the mathematic portion

if(x1 == x2 or x1 == -x2):
  yvalue = (b1-b2) / (y1-y2)
  xvalue = (b1 - (y1*yvalue)) / x1
elif(y1 == y2):
    xvalue = (b1-b2) / (x1-x2)
    yvalue = (b1 - (x1*xvalue)) / y1
else:
  subx1 = x1
  x1 *= x2
  y1 *= x2
  b1 *= x2
  x2 *= subx1
  y2 *= subx1
  b2 *= subx1
  yvalue = (b1-b2) / (y1-y2)
  xvalue = (b1 - (y1*yvalue)) / x1
print("The value of x is equal to:", xvalue, "\nThe value of y is equal to:", yvalue)