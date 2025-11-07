# marks=[]
# f1=input("enter the marks:")
# marks.append(f1)
# f2=input("enter the marks:")
# marks.append(f2)
# f3=input("enter the marks:")
# marks.append(f3)
# print(marks)
# marks.sort()
# print(marks)
# t=[1,2,34,556,54]
# print(sum(t))
#practice
#Empty list
s=set()
s1={1,2,3,4}
s2={1,"Apple",3.12,(1,2)}
print(s2)
s3={1,2,2,3,4}
print(s3)

for ele in s1:
    print(ele)

#Add a single element
s1.add(6)
print(s1)
#add multiple elements
s1.update([4,2,1])
print(s1)
#can also add tuples
s1.update((98,9))
print(s1)
    