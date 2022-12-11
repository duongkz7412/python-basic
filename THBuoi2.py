#nguyen dai duong b2016953
#cau 1
def cau1():
    for i in range(100,301):
        if i%2==0:
            if i==300:
                print(i)
                break
            print(i,end=', ')
#cau 2
from array import *
def cau2():
    str=input("Nhap vao day so cach nhau boi dau phay: ")
    arr= str.split(',')
    for i in arr:
        if int(i)%2==1:
            print(i, end=',')
#cau 3
def cau3():
    data={}
    for i in range(20):
        data[i]=i+1
        value=pow(data[i],2)
        data.get(value)
        print(data[i],"-",value)
#cau 4
def cau4():
    list = [12,24,45,70,88,120,155]
    list.remove(list[0])
    list.remove(list[4-1])
    list.remove(list[5-2])
    print(list)
#cau 5
def cau5():
    list1=[12,3,6,78,35,55,120]
    list2=[12,24,35,78,88,120,155]
    list3=[]
    for i in list1:
        for j in list2:
            if i==j:
                list3.append(i)
    print(list3)
#cau 6
def cau6():
    for i in range(6,21):
        print(i*i)

def check(n):
    for i in range(len(n)):
        if not(str(n[i]).isdecimal()):
            return 0
    return 1
#cau 7
def cau7():
    while True:
        n=tuple(input("Nhap vao so day so ngan cach boi dau phay: ").split(','))
        if check(n):
            break
    for i in range(len(n)):
        if int(n[i])%2==0:
            print(n[i], end=' ')

def khong_trung(letters):
    result=""
    for i in letters:
        if i not in result:
            result+=i
    return result

def count(letters):
    dic={}
    str=khong_trung(letters)
    for i in range(len(str)):
        dem=letters.count(str[i])
        dic[str[i]]=dem

    print(dic)
#cau 8
def cau8():
    letters=input("Nhap vao mot cau: ")
    count(letters)
#cau 9
def cau9():
    ls=[]
    letters = input("Nhap vao mot cau: ")
    ls=list(reversed(letters))
    for i in ls:
        print(i,end='')
#cau 10
def cau10():
    while True:
        str = input("Nhap vao mot cau: ")
        if len(str)>=2:
            break
    for i in range(len(str)):
        if i<2:
            print(str[i],end='')
        if i>len(str)-3:
            print(str[i],end='')
#cau 11
def cau11():
    str1 = input("Nhap vao mot cau: ")
    str2 = input("Nhap vao mot cau: ")
    tmp=str1[:2]
    str1=str2[:2]+str1[2:]
    str2=tmp[:2]+str2[2:]
    str3=str1+' '+str2
    print(str3)
#cau 13
def cau13():
    str = input("Nhap vao mot cau: ")
    for i in range(len(str)):
        if str[i]==str[0]:
            str2=str.replace(str[i],'@')
    print(str[0]+str2[1:])