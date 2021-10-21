#!/usr/bin/env python
# coding: utf-8

# - NUmber

# In[3]:


1+1


# In[4]:


2/3


# In[5]:


2%6


# In[6]:


2*6


# In[8]:


2**6 #2 power 6 


# In[9]:


79-89


# In[10]:


40 * 'Chandni'


# In[12]:


10* 'Chandni' 


# In[14]:


type(1)


# In[15]:


type(7.8)


# In[19]:


type('str')


# In[21]:


type(True)


#  - Variable Assignmnet

# In[22]:


a = 10
type(a)


# In[23]:


a= 'Hello'
type(a)


# In[24]:


a = 10
b= 20
print(a+b)
print(a*b)
print(a/b)
print(a-b)
print((a*b)*(a/b))


# In[26]:


first_name='Chandni'
Last_name="Sindhav"
print("my first name is {} and last name is {}".format(first_name,Last_name))
print("my first name is {first} and last name is {last}".format(first=first_name,last=Last_name))


# In[27]:


len("Chandni")


# In[28]:


type(['Chandni',"Sindhav",1,2,3.5,5,True])


# In[29]:


list_Demo=['Chandni',"Sindhav",1,2,3.5,5,True]


# In[30]:


list_Demo


# In[31]:


list_Demo.append(4)


# In[32]:


list_Demo


# In[33]:


len(list_Demo)


# In[34]:


list_Demo[2]


# In[41]:


list_Demo.index(4)


# In[44]:


list_Demo.insert(0,'Champ')


# In[45]:


list_Demo


# In[46]:


list_Demo[:]


# In[50]:


list_Demo[0:5]


# In[51]:


list_Demo[1:]


# In[52]:


list_Demo.append(['Hello',6])


# In[53]:


list_Demo


# In[54]:


list_Demo1 = [1,2,3,4,5,"Chandni","Gem"]


# In[55]:


list_Demo1


# In[57]:


list_Demo1.extend(["Sindhav",7,89,0])


# In[58]:


list_Demo1


# In[59]:


list_Demo


# In[61]:


print(list_Demo)
print(list_Demo1)


# In[63]:


list_Demo.pop() #bydefault last element dlete


# In[64]:


list_Demo


# In[65]:


list_Demo.pop(0)


# In[66]:


list_Demo


# In[68]:


list


# In[70]:


list_co=[1,2,3,4,5,6,1,1,3,4,5,6,2,3]


# In[73]:


list_co.count(1) #occurance of perticular number in list


# In[74]:


min(list_co)


# In[75]:


max(list_co)


# In[76]:


list_co * 3 #list appended 3 times


# In[79]:


list_co.clear()


# In[80]:


list_co


# In[85]:


list_co = [1,2,3,4,5]


# In[86]:


list_co


# - Set

# In[87]:


set1={1,2,3,3}


# In[88]:


set1


# In[92]:


set1.add(4)


# In[93]:


set1


# In[94]:


set2={1,2,3,5,6,7,'Hello'}


# In[95]:


set2


# In[96]:


set1.difference(set2)


# In[98]:


set2.difference(set1)


# In[99]:


set1


# In[100]:


set2


# In[101]:


set2.intersection(set1)


# In[102]:


set2


# In[103]:


set2.intersection_update(set1)


# In[104]:


set2


# In[105]:


set2.issubset(set1)


# In[107]:


set2.add(5)


# In[108]:


set2.add(6)


# In[109]:


set2


# In[110]:


set2.issubset(set1)


# In[111]:


set1.issubset(set2)


# In[112]:


set1


# In[128]:


for x in set1:
    print(x)


# In[113]:


set1.issuperset(set2)


# In[114]:


set2.issuperset(set1)


# - Dictionary

# In[115]:


dc ={}


# In[116]:


type(dc)


# In[117]:


dc={1,2,3,4}


# In[118]:


type(dc)


# In[119]:


dc={"Name":"Chandni","Surname":"Sindhav","LName":"A"}


# In[120]:


type(dc)


# In[121]:


dc.get(0)


# In[122]:


dc


# In[123]:


dc.get(1)


# In[124]:


dc.items()


# In[130]:


dc['Name']


# In[131]:


for x in dc:
    print(x)


# In[132]:


for x in dc.values():
    print(x)


# In[133]:


for x in dc.items():
    print(x)


# In[145]:


NameFirst={'Chandni':'Dax'}
SurnameAll={'Sindhav':'Chavda'}
NameLast={'A':'P'}


# In[146]:


dc={'Name':NameFirst,'Surname':SurnameAll,'LName':NameLast}


# In[147]:


dc


# In[148]:


dc['Name']


# In[149]:


print(dc['Name']['Chandni'])


# - Tuples

# In[150]:


tuples_demo=(1,2,3,4)


# In[152]:


type(tuples_demo)


# In[ ]:


tuples_demo


# In[6]:


prices = [10,20,30]
count = 0
for item in prices:
    count += item
print(count)


# In[8]:


for x in range(5):
    for y in range(5):
        print(x,y)


# In[14]:


numbers = [5,2,5]
for x in numbers:
    for y in range(x):
        print(x)


# In[33]:


numbers = [2,409867,500,6,7,19,40]
tmp = 0
for x in numbers:
   if x > tmp:
        tmp = x
print(tmp)


# In[40]:


numbers = [5,4,3,7,8,9,10,5,4,3,10,10]


# In[35]:


numbers


# In[36]:


numbers.sort()


# In[37]:


numbers


# In[41]:


numbers.count(10)


# In[43]:


unique = []
for x in numbers:
    if x not in unique:
        unique.append(x)
unique        


# # palindrome

# In[80]:


Number = input("Enter Number or string to check is palindrom or not:")
print("Number " + Number)

Alist=[]
for x in str(Number):
    Alist.append(x)
print(Alist)
arev = list(reversed(Alist))
# other way
# Directly converted to list arev = list(reversed(Number)) not need to run loop
print(arev)
if(Alist == arev):
    print("Number is palindrom")
else:
    print("Not palindrom")


# # fibonassi
# 

# In[82]:


limit = 5 
prev = 1
j =0
tmp = 0

for i in range(limit): 
    tmp = j + prev
    j =  prev
    prev = tmp
    print(tmp)
    


# # same value howmany times iterate in the loop

# In[131]:


arr= [11,12,11,12,45,56,45,45,12,45,45,67,89,12]
arr.count(12)

# Using in build count function
# for i in arr:
#     count=arr.count(i)
#     print("value : ",i,"  Repeted  :",count)

# without inbuild function
for i in arr:
    count=0
    for x in arr:
        if i == x:
            count=count+1
    print("value : ",i,"  Repeted  :",count)
    


# # Factorial

# In[17]:


limit = input()
limit = int(limit)
  
tmp=1
tmpc=0
for i in range(1,limit+1):
    i = i*tmp
    tmp = i
    tmpc=tmp
print("Factorial of : " , limit," is : " ,tmpc)


# # max number
# 

# In[4]:


firstNumber = input("Enter first Number :")
print("Number " + firstNumber)
secondNumber = input("Enter second Number :")
print("Number "+ secondNumber)
if(firstNumber > secondNumber):
    print("firstNumber is greater than secondNumber")
elif(firstNumber == secondNumber):
    print("firstNumber and secondNumber both are equal")
else:
    print("secondNumber is greater than firstNumber")


# # buzz

# In[14]:


firstNumber = input("Enter first Number :")
print("Number " + firstNumber)
number = int(firstNumber)

if(number % 3 == 0):
    print("by 3")
if(number % 5 == 0):
    print("by 5")
if(number % 3 == 0 and number % 5 ==0):
        print("by both")
else:
    print("Number : "+ firstNumber)


# # swap
# 

# In[19]:


firstNumber = input("Enter value of A :")
secondNumber = input("Enter Value of B :")
A = int(firstNumber)
B = int(secondNumber)
print("Before swap A: ",A)
print("Before swap B: ",B)
A = A+B 
# A= 10+20=30
B = A-B
# B= 30-20 = 10
A = A-B
# A= 30-10
print("After swap A: ",A)
print("After swap B: ",B)


# # for loop

# In[29]:


firstNumber = input("Enter value of A :")
limit = int(firstNumber)
for i in range(limit+1):
    print("*"*i)


# # array

# In[30]:


lst = []
n = int(input("Enter number of elements : ")) 
# iterating till the range
for i in range(0, n):
    ele = int(input())
    lst.append(ele) # adding the element
print(lst)


# In[105]:


def arrayOperation(lst1):
    tmp=0
    for i in lst1:
        if(i>tmp):
            tmp=i
    print("Greater element in array is :- ",tmp)
    lstReverse=[]
    print("Reverse ==========")
    for i in range(len(lst1)-1,-1,-1):
        print(lst1[i]) 
    print("sorting ==========")
    tmpsort =0
   
    for i in range(len(lst1)):
        for y in range(i,len(lst1)):
            if(lst1[y]>lst1[i]):
                tmpsort= lst1[i]
        print(tmpsort)
        
        
arrayOperation(lst)


# In[ ]:





# In[ ]:




