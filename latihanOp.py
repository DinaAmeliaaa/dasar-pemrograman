#Operator
#Operator Aritmatika
a = 5
b = 3
c = 8
d = 6
e = 2
penjumlahan = a + b + c
sisabagi = c % a
perkalian = d * e
pengurangan = c - d
pembagian = a / b 
perpangkatan = c ** e
pembagianbulat = a // b
print(f"hasil penjumlahan {a} + {b} + {c} = {penjumlahan} \n"
      f"sisa bagi {c} mod {a} = {sisabagi} \n"
      f"perkalian {d} * {e} = {perkalian} \n"
      f"pengurangan {c} - {d} = {pengurangan} \n"
      f"pembagian {a} / {b} = {pembagian} \n"
      f"perpangkatan {c} ** {e} = {perpangkatan} \n"
      f"pembagian bulat {a} // {b} = {pembagianbulat}" )

#Operatorassignment

a += 2 #a = 5 + 2
a **= 2 #a = 7 ** 2
print(a)

#Operator perbandingan
perbandingan = a >= b # 56 >= 2 true 

x = 3
y = 2
banding = x <= y

print(x == y)
print(banding)

#Operator logika AND
opAnd = perbandingan and banding #false
opOR = perbandingan or banding #true
opNot = not opOR #false
opNot = not opAnd #true
print(opAnd)
print(opOR)
print(opNot)