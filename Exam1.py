import sys


print(sys.version)
print("Hello Python")
print("Very Simple")

a = 1
b = 3

print(a+b)
helloString = "Hello Python"
print("a+"+helloString+" dosen't work")
print("str(a)+"+helloString+" working")
print(str(a)+helloString)

c = a*b
print(str(a)+" * "+str(b)+"="+str(c))
c = a/b
print(str(a)+" / "+str(b)+"="+str(c))
c = a % b
print(str(a)+" % "+str(b)+"="+str(c))
c -= a
print("c -= a ="+str(c))

del c
print("c is deleted.")


# 함수 선언시(def) 이전에 2개의 개행필요
def MyFirstFunction(h):
    print("MyFirstFunction Called")
    print(h)


MyFirstFunction(a)
MyFirstFunction(b)

# 지역 변수 전역 변수 같음
# print(h)에서 h는 undefined임
