def cal(op,x,y):
  if op=='+':
    return x+y
  elif op=="-":
    return x-y
  elif op=='*':
    return x*y
  elif op=='/':  
    return x/y
  elif op=='^':
    return x**y
  else:
    return "Invalid operator"
while True:
  print("Enter '+'for add,'-'for sub,'*'for mul,'/'for div,'^'for power")
  op=input("Enter the operator:")
  x=int(input("Enter the first number:"))
  y=int(input("Enter the second number:"))
  print(cal(op,x,y))
  print("do you want to continue")
  choice=input("Enter 'y'for yes,'n'for no:")
  if choice=='n':
    break
  else:
    continue
  