lesson2="lists and  tuple"
fr1="lists"#a built in data type that store set of value..(string,loop ,float,integars etc)
marks=[95.5,84.5,74.5,66.5,45.5] #this is called list
print(marks)
print(type(marks))
print(marks[0])
print(marks[4])
print(len(marks)) #in python we can store different type of data in a list.
student=["Maham",23 ,95.5,"Pakistan"]
print(student[0])
#string and lists have this difference string is immutable while list is mutable we can easily makes changes in it
#in string in index value access is allowed but change is not allowed
#but in list it is totally acceptable
student[0]="Maham Arshad"
print(student)
fr2="list slicing"
#list-name[staring_idx:ending_idx] ending index not include
print(marks[0:4])
print(marks[ :4])
print(marks[4: ])#it is just string slicing
#here also have negative index
print(marks[-3:-1])
#methods or function methods are specific
#1)list.append() add one element in list
marks.append(56.5)
print(marks)#this is called mutating the list
#2)list.sort() sort in ascending order
marks.sort()
print(marks)
#3)list.sort(reverse=True) sort in descending order
marks.sort(reverse=True)
print(marks)
#4)list.reverse() it reverse the list
marks.reverse()
print(marks)
#in string the sorting is according alphabets like(a,b,c.....)
list=["ca","bb","ac"]#so here sorting is according to alphabets
list.sort()
print(list)
#5)list.insert(idx,el) insert elements at index
marks.insert(3,78.5)
print(marks)
#6)list.remove(1) remove occurence of elements
marks.remove(78.5)
print(marks)
fr3="Tuples"
#a built in data type that lets us create immutable sequences of values
#to create tuple we need to used these bracket ()
tup=(2,6,8,67,89)
print(type(tup)) #tuple must need comma (2,) single value need comma
#indexing
print(tup[1:4])
#methods in tuple
#1)tup.index(el) returns index  of first occurence
tup2=(2,3,1,1)
print(tup2.index(1))
#2)tup.count(el) counts total occurence
print(tup2.count(3))
fr4="Practice"
#1) WAP to ask the user to enter names of their 3 favorite movies & store them in a list
""""
movies=[]
mov1= input("fm1:")
mov2= input("fm2:")
mov3= input("fm3:")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)
"""     
#2)WAP to check if a list contains a palindrome of elements.(Hint:use copy() method)
#the string that is same from start and end ma'ma here end and start same
list5=[1,2,1]
list6=[1,2,3]
copy_list5=list5.copy()
copy_list5.reverse()
if(copy_list5==list5):
    print("palindom")
else:
    print("not")    
copy_list6=list6.copy()
copy_list6.reverse()
if(copy_list6==list6):
    print("pandulim")
else:
    print("not") 
#3)WAP to count the number of students with the "A" grade in the following tuple.
# Store the above values in a list &sort them from "a" to "d"
tup8=("c","d","a","a","b","b","a")
print(tup8.count("a"))       
#part2
list8=["c","d","a","a","b","b","a"]
list8.sort()
print(list8)