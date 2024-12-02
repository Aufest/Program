import random as rd

a = [1,2,3,4,5,6,7,8,9,0]
success = [0,1,2,3,4,5,6,7,8,9]


while a != success:
  check = [0,0,0,0,0,0,0,0,0,0]
  n = 0
  for i in range(len(a)):
    addr = 0
    j = 0
    num = rd.randint(0,len(a)-i-1)
    tmp = a[n]
    while j != num:
      if check[addr] == 0:
        j += 1
      addr += 1
    a[n] = a[num]
    a[num] = tmp
    check[addr] = 1
    n += 1
  print("{} {}".format(a,a != success))
  
print("ソートが終わりました:{}".format(a))

    


