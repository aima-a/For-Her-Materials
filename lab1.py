start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

for i in range(start, end+1):
  if i % 2 == 0:
    print(i)