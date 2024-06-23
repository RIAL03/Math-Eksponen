main = input("Mau cari nilai? yes / no")

while(main=="yes"):
  inputUser = int(float(input("Masukan angka :")))
  pangkat2 = 0
  pangkat3 = 0
  pangkat5 = 0

  nilai2 = inputUser
  while nilai2 % 2 == 0 :
    nilai2 /= 2
    pangkat2 += 1
  
  nilai3 = nilai2
  while nilai3 % 3 == 0:
    nilai3 /= 3
    pangkat3 += 1
  
  nilai5 = nilai3
  while nilai5 % 5 == 0:
    nilai5 /= 5
    pangkat5 += 1
  
  if(pangkat2 >= 1 and pangkat3 >= 1 and pangkat5 >= 1 and nilai5 == 1):
    print(f"2^{pangkat2} x 3^{pangkat3} x 5^{pangkat5}")
    
  elif(pangkat2 >= 1 and pangkat3 >= 1 and pangkat5 >= 1 and nilai5 > 1):
    print(f"2^{pangkat2} x 3^{pangkat3} x 5^{pangkat5} x {nilai5}")

  elif(pangkat2 >= 1 and pangkat3 >= 1 and nilai3 == 1):
    print(f"2^{pangkat2} x 3^{pangkat3}")
    
  elif(pangkat2 >= 1 and pangkat5 >= 1 and nilai5 == 1):
    print(f"2^{pangkat2} x 5^{pangkat5}")
  
  elif(pangkat2 >= 1 and pangkat5 >= 1 and nilai5 > 1):
    print(f"2^{pangkat2} x 5^{pangkat5} x {nilai5}")
  
  elif(pangkat3 >= 1 and pangkat5 >= 1 and nilai5 == 1):
    print(f"3^{pangkat3} x 5^{pangkat5}")
  
  elif(pangkat3 >= 1 and pangkat5 >= 1 and nilai5 > 1):
    print(f"3^{pangkat3} x 5^{pangkat5} x {nilai5}")
  
  elif(pangkat2 >= 1 and nilai2 == 1):
    print(f"2^{pangkat2}")

  elif(pangkat2 >= 1 and nilai2 > 1):
    print(f"2^{pangkat2} x {nilai2}")
  
  elif(pangkat3 >= 1 and nilai3 == 1):
    print(f"3^{pangkat3}")

  elif(pangkat3 >= 1 and nilai3 > 1):
    print(f"3^{pangkat3} x {nilai3}")
    
  elif(pangkat5 >= 1 and nilai5 == 1):
    print(f"5^{pangkat5}")
    
  elif(pangkat5 >= 1 and nilai5 > 1):
    print(f"5^{pangkat5} x {nilai5}")
  
  elif(pangkat2 == 0 and nilai2 > 1):
    print(f"{inputUser}")
  
  else: print("Sorry Wrong")
print("Terima Kasih")
  


  