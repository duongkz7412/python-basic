#Nguyen Dai Duong B2016953
#Bai 1
v = input()
print("Hello",v,"Welcome to Python" )
#Bai 2
print("Nhập vào một số:")
n=int(input())
while n<0 or n>10:
   n=int(input("Sai điều kiện. Nhập lại n :"))
n= n+ (n*11) + (n*111) +(n*1111)
print(n);
#Bai 3
print("Nhập a,b : ")
a=int(input())
b=int(input())
while b==0 :
   print("Nhập lại b: ")
   b=int(input())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
#Bai 4
import math
print("Nhập bán kính hình tròn:")
r = float(input())
cv = 2*math.pi*r
dt = pow(r,2)
print("Chu vi hình tròn bằng: ", cv)
print("Diện tích hình tròn bằng: ", dt)
#Bai 5
n = int(input("Nhập n:"))
while n<0:
   print("Nhập lại n :")
   n=int(input())
def giaiThua(n):
   if n == 0:
      return 1
   return n * giaiThua(n - 1)
print(giaiThua(n))
#Bai 6
import math
def giaiPTBac2(a, b, c):
   if (a == 0):
      if (b == 0):
         print("Phương trình vô nghiệm!");
      else:
         print("Phương trình có một nghiệm: x = ", + (-c / b));
      return;
   delta = b * b - 4 * a * c;

   if (delta > 0):
      x1 = (float)((-b + math.sqrt(delta)) / (2 * a));
      x2 = (float)((-b - math.sqrt(delta)) / (2 * a));
      print("Phương trình có 2 nghiệm là: x1 = ", x1, " và x2 = ", x2);
   elif (delta == 0):
      x1 = (-b / (2 * a));
      print("Phương trình có nghiệm kép: x1 = x2 = ", x1);
   else:
      print("Phương trình vô nghiệm!");

a = float(input("a = "));
b = float(input("b = "));
c = float(input("c = "));
giaiPTBac2(a, b, c)
Bai 7
a=[]
for i in range(5000,7000):
    if(i%7==0) and (i%5!=0):
        a.append(str(i))
print(','.join(a))
#Bai 8
n = int(input("Nhập n:"))
while (n<=0):
    n = int(input("Nhập vào n>0: "))
x = n
ketQua = ""
while(n>0):
    ketQua = str(n%2)+ketQua
    n = n//2
print("Kết quả: ", ketQua)
#Bai 9
def uscln(a, b):
   temp1 = a;
   temp2 = b;
   while (temp1 != temp2):
      if (temp1 > temp2):
         temp1 -= temp2;
      else:
         temp2 -= temp1;
   uscln = temp1;
   return uscln;

def bscnn(a, b):
   return int((a * b) / uscln(a, b));


a = int(input("a = "));
b = int(input("b = "));

print("Ước số chung lớn nhất của", a, "và", b, "là:", uscln(a, b));

print("Bội số chung nhỏ nhất của", a, "và", b, "là:", bscnn(a, b));
#Bai 10
import math

def kiemtrangto(n):
   if (n < 2):
      return False;
   squareRoot = int(math.sqrt(n));
   for i in range(2, squareRoot + 1):
      if (n % i == 0):
         return False;
   return True;
n = int(input("Nhập n = "));
print ("Tất cả các số nguyên tố nhỏ hơn", n, ":");
sb = "";
if (n >= 2):
    sb = sb + "2" + " ";
for i in range (3, n+1):
    if (kiemtrangto(i)):
        sb = sb + str(i) + " ";
    i = i + 2;
print(sb);
#Bai 11
import math

def kiemtrangto(n):
   if (n < 2):
      return False;
   squareRoot = int(math.sqrt(n));
   for i in range(2, squareRoot + 1):
      if (n % i == 0):
         return False;
   return True;

print ("Liệt kê tất cả số nguyên tố có 4 chữ số:");
dem = 0;
for i in range(1001, 9999):
    if (kiemtrangto(i)):
        print(i);
#Bai 12
def tong(n):
   total = 0;
   while (n > 0):
      total = total + n % 10;
      n = int(n / 10);
   return total;

n = int(input("Nhập n :"));
while n<0:
   n=int(input("Nhập lại n:"))
print("Tổng các chữ số của", n, ":", tong(n));
#Bai 13
a=[]
s = 0
for i in range(1000, 2000):
    if i % 2 != 0:
         a.append(str(i))
print(','.join(a))

#Bai 14
n = int(input("Nhập n"))
s = 0
for i in range(0, n):
   s += i/(i + 1)
print(s)
#Bai 15
import math as m
from array import *

def Entropy(arr):
    e=0
    for i in range(len(arr)):
        e-=arr[i]*m.log2(arr[i])
    return e
n=int(input("Enter n: "))
arr=array('f',[])
for i in range(n):
    x=float(input("Enter your num: "))
    arr.append(x)
print(Entropy(arr))

#Bai 16
import math as m
from array import *

def Entropy(arr):
    e=0
    for i in range(len(arr)):
        if arr[i]!=0:
            e-=arr[i]*m.log2(arr[i])
    return e

X=array('f',[1/14,1/14,3/14,3/14])
HX=Entropy(X)
print("H(X): ",HX)
Yx1=array('f',[1/4,2/4,1/4,0])
Yx2=array('f',[1/4,2/4,1/4,0])
Yx3=array('f',[1/8,3/8,3/8,1/8])
Yx4=array('f',[1/8,3/8,3/8,1/8])
HYx1=Entropy(Yx1)
HYx2=Entropy(Yx2)
HYx3=Entropy(Yx3)
HYx4=Entropy(Yx4)
print("H(Y/X=x1): ",Entropy(Yx1))
print("H(Y/X=x2): ",Entropy(Yx2))
print("H(Y/X=x3): ",Entropy(Yx3))
print("H(Y/X=x4): ",Entropy(Yx4))
entropy=array('f',[HYx1,HYx2,HYx3,HYx4])
HYX=0
for i in range(len(X)):
    HYX+=X[i]*entropy[i]
print("H(Y/X): ", HYX)

Y=array('f',[])
for i in range(len(X)):
    x=X[i]*Yx1[i]+X[i]*Yx2[i]+X[i]*Yx3[i]+X[i]*Yx4[i]
    Y.append(x)
HY=Entropy(Y)
print("H(Y): ",Entropy(Y))
print("I(Y/X): ",HY-HYX)