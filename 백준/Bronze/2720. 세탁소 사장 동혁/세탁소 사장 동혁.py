
result =[]
data = []
for i in range(int(input())):
  data.append(int(input()))
  

for i in data:
  row = []
  quarter = i // 25
  quarterRemainder = i%25
  row.append(quarter)
  if(quarterRemainder > 0):
    dime = quarterRemainder // 10
    dimeRemainder = quarterRemainder %10
    row.append(dime)
    if(dimeRemainder > 0):
      nickel = dimeRemainder // 5
      penny = dimeRemainder % 5
      row.append(nickel)
      row.append(penny)
    else:
      row.append(0)
      row.append(0)  
  else:
    row.append(0)
    row.append(0)
    row.append(0)
    
  result.append(row)
    
for row in result:
  print(*row)


