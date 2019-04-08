#Mitchell Taylor | Lab 01 | Dr. Sethi | 22, January 2018

#1
def division():
  print("\nNow running the division function\n")
  x = 0
  y = 1
  x = int(input("Please enter your first digit\n"))
  y = int(input("Please enter your second digit\n"))
  z = x/y
  print("Your answer is ",z)

def truncation():
  print("\nNow running the truncation function\n")
  x = 0
  y = 1
  x = int(input("Please enter your first digit\n"))
  y = int(input("Please enter your second digit\n"))
  z = x//y
  print("Your answer is", z)
  
division()
truncation()

#2
def tempConverter():
  print("\nNow running the temperature conversion function\n")
  convertFactor = int(input("\nPlease enter 1 to convert from Celius to Farenheit, 2 for Farenheit to Celcius, anything else to quit\n"))
  if convertFactor == 1:
    tempC = int(input("Please input the temperature in Celcius: \n"))
    tempF = tempC / (5.0 / 9.0) + 32.0
    print(tempC, " C = ", tempF, " F")
  elif convertFactor == 2:
    tempF = int(input("Input the temperature in Farenheit: \n"))
    tempC = (5.0/9.0) * (tempF - 32.0)
    print(tempF, " F = ", tempC, " C")
  else:
    print("\nOkay, quitting.\n")
    
tempConverter()

#3
def factPrint():
  print("\nNow running the factorial printing function\n")
  a = 1
  b = 0
  c = int(input("Please input your desired factorial\n"))
  while b < c:
    b = b+1
    a = a * b
    print(b, "! = ", a)
factPrint()

#4
def factPrintLimited():
  print("\nNow running the factorial printing (Limited) function\n")
  a = 1
  b = 0
  c = int(input("Please input your desired factorial\n"))
  while b < c:
    b = b+1
    a = a * b
    if a > 1000000000:
      b = c
      print("\nSorry this program will not print values exceeding 1,000,000,000!\n")
    else:
      print(b, "! = ", a)

factPrintLimited()


x = int(input("Please enter your desired factorial\n"))
facs = [facs[-1] for i in range(1,x) if not facs.append(i*facs[-1] if facs else 1)]
print(facs)
