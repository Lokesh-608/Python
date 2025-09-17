t = int(input("Enter temperature: "))
if t < 20:
  print("cold")
  if 20 <= t <= 30:
    print("pleasant")
    if t > 30:
      print("hot")


