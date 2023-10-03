sum = 0

num = int(input("Enter a number: "))

while num >= 0:

  if num % 2 == 0:
      sum += num

  num = int(input("Enter a number: "))

print("The sum of even numbers is:", sum)