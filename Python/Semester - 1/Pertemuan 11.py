#Challange 1
print("=====Challange 1=====")
Num1= int(input("Masukkan Num1: "))
if (Num1 >10):
    print("This is over 10")
elif (Num1 == 10 ):
    print("This is squal to 10")
else:
    print("This is under 10")
print("")

#Challange 2
print("=====Challange 2=====")
l, u, p, d = 0, 0, 0, 0
Pass = input("Masukkan Password Anda : ")
hurufkapital="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
hurufbiasa="abcdefghijklmnopqrstuvwxyz"
simbol="$#@"
angka="0123456789"
if (len(Pass) >= 6):
    for i in Pass:
        if (i in hurufbiasa):
            l+=1           
        if (i in hurufkapital):
            u+=1           
        if (i in angka):
            d+=1         
        if(i in simbol):
            p+=1       
if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(Pass)):
    print("Valid Password")
else:
    print("Invalid Password")
print("")

#Challanges 3
print("=====Challange 3=====")
angka = (1, 2, 3, 4, 5, 6, 7, 8, 9)
arrgenap=[]
arrganjil=[]

for i in angka:
    if i%2==0:
        arrgenap.append(i)
    elif i%2==1:
        arrganjil.append(i)

print("array genap :" ,arrgenap)
print("panjang array genap " ,len(arrgenap))
print("array ganjil :" ,arrganjil)
print("panjang array ganjil ",len(arrganjil))
print("")

## Challange 4
print("=====Challange 4=====")
def turtle ():
 import turtle

 for i in range(0,360):
    turtle.forward(1)
    turtle.right(1)

 turtle.exitonclick()

def turtle_2():
 import turtle
 import random

 for i in range(0,8):
    for i in range(0,8):
        turtle.forward(50)
        turtle.right(45)
        
    turtle.right(36)
 turtle.hideturtle()
 turtle.exitonclick()

def turtle_3():
 import turtle
 import random

 turtle.pensize(3)
 for i in range(0,8):
    turtle.color(random.choice(["Red", "Blue", "Yellow", "Green"]))
    turtle.forward(50)
    turtle.right(45)
 turtle.exitonclick()
    
# #Challanges 5
print("------Challange 5------")
from datetime import datetime, timedelta
import datetime
now = datetime.datetime.now()
print("------")

print("Waktu hari ini = ", now)
print("Tahun = ", now.year)
print("Bulan = ", now.month)
print("Hari = ", now.day)
print("Jam = ", now.hour)
print("Menit = ", now.minute)
print("Detik = ", now.second)

print("--------")
print("1 minggu yang lalu adalah: ", now - datetime.timedelta(weeks=1))
print("100 hari yang lalu adalah: ", now - datetime.timedelta(days=100))
print("1 minggu kedepan: ", now + datetime.timedelta(weeks=1))
print("1000 hari dari sekarang: ", now +  datetime.timedelta(days=1000))

print("--------")
birthday = datetime.datetime(2022,12,30)

print("Hitung mundur hari ulang tahun... ", now -  birthday)
print("--------")
print("")

#Challange 7
print("-----Challange7-----")
def fibonnaci(n):
    if n == 0 :
        return 1
    elif n == 1 :
        return 1
    else :
        return fibonnaci(n-1) + fibonnaci(n-2)
    
for i in range(8):
    print(fibonnaci(i), end=" ")
        

turtle_3()



