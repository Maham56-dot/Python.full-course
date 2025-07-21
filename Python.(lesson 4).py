lesson4:"Loops" # loops are used to repeat instrction
#types 1) for loops 2)while loops
#2) while loops (some work) this will not action untill this condition satisfy
"""
count =1
while count<= 5: #if this condition false then loop stop otherwise it will not stop
    print("hello")
    count+=1 #here we used Iterator. running in loop this function is known as iteration
print(count) 
"""
"""
i=1
while i<=5:#by using this you can print 
    print("maham")
    i+=1
print(i)    
#start printing number
i=1 #here we print counting
while i <=5:
    print(i)
    i+=1
i=5
while i >= 1 :#here we reverse  it
    print(i) 
    i-=1 
"""    

#1) print numbers from 1 to 100
"""
i=1
while i <=100:
    print(i) 
    i+=1   
"""
#2) print numbers from 100 to 1
"""
i=100
while i>=1:
    print(i)
    i-=1
    """
#3)print multiplication table of number n. think here  we are printing table
"""
n=int(input("enter integars:"))
i=1
while i<=10:
    print(n*i)
    i+=1
"""    
#4)print the elements of the following list using aloop:
"""
num= [1,4,9,16,25,36,49,64,81,100] #this is called traverse.its travelling in code
idex= 0
while idex<len(num):
    print(num[idex])
    idex+=1
"""    
#5)Search for a number x in this tuple using loop:
"""
num3=(1,4,9,16,25,36,49,64,81,100)
x=36
i=0
while i< len(num3):
    if(num3[i]==x):
        print("found:",i)
    
    i+=1
"""
#Break and continue kryword
#1)Break  #2)continue
#1)Break (used to terminate loop when encountered)
"""  
i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1
"""
#2)continue(terminates execution in current iteration & continues execution of loop with next iteration)
"""
i=0
while i<= 5:
    if(i==3):
        i+=1

        continue
    print(i)
    i+=1
"""
#for loop in python(used for sequential traversal .for trasversal list ,string,tuples etc)
#1) for loops    #2) for loop with else
#1)for loops
"""
list =[1,2,3,4]
for num in list:
    print(num)
fruit=["apple","orange","banana"] 
for word in fruit:
    print(word)
#tuple
fruit2= ("mango","orange","pineapple")   
for words in fruit2:
    print(fruit2)
"""            
#practice 
#Q1:print the element of the following list using a loop
"""
num4=[1,2,3,4,5]
for el in num4:
    print(el)
"""    
#q2: search for number x in the tuple using loop.this is called linear search.
""" 
n=(1,4,9,16,25,36,49,64,81,100,36)
x=36
idx = 0
for el in n:
    if(el == x):
        print("found",idx)
    idx += 1 
"""
#range()
# range functions returns sequence of num,starting from 0 by default and increments by 1 (by default) and stops before specifie number
#range (start? , stop ,step?)
"""
seq1=range(5)#this is first(range ,stop)
seq = range(2,5)#range(start,stop)
for i in seq:
    print(i)
seq1 = range(2,5,2)#range(start,stop,step)
for i in seq1:
    print(i) 
"""  
#pass statement.pass is a null state that does nothing.placeholder for future.
for i in range (5):
    pass
print("imp work")           
        