lesson1="python basics"
print("Python course")
class1="print function"#print function is used to print any output you ask to print as it is.
part1="I printed Maham Arshad but I learn english must be in quotes"#remember in this function i am printing what i want i need exact  output
a="here I found out about integars that integars and decimals not use double quotes"
#we use integars as it is like print=45 
b="here I also learn about +,-,* we can do these calculations" 
#I learn how to do  calculation in it.I am happy this is my lesson of python.
part2="variables"#in this we give name to our location program.or we simply store any value.
a="I store the name=maham arshad as variable here I learn if you add english use it in inverted comma but integars are not in inverted comma"
#I have learn that if you used print method to get variable value any variable at that momemt print function comma removed
name="Maham Arshad"#this is called string. here we use inverted commas for my name.so any english sentence,words,paragraph while making variable use inverted comma
age=34#this is also string but for integars.now here is intergars so we are not using inverted commas.
print(name)#now if you want to get value of variable so at that time you have use print function without comma.
print("my name is:",name)#so if you want to print whole and want to get so separated it in this way.
part3="assignment operator"#this is value store so in previous we see age=25 so here it goes from left to write means age is 25
age2=age #if we use in this way then the value of age variable is stored in age2 value so always age variable value came.
indentifiers=("myVariable,variable1,variable-for-print...etc")
#if we use variables so here is rules how to write name variables never put digits at number at start of variable name
#do not use extra symbols
# #these are two variables name and age
name="Maham Arshad"
age=23
price=25.33
part4="type"#type inpython tells us about the class means is it string(sentence,words),integar(numbers) or float(means decimals)
print(type(name))
print(type(age))
print(type(price))#type is data type.there are so many data type but most important is five(string,integar,float,boolean,none)
a="Data Type"
#1)integars(eg(34,-67,1,-6 means any no)),2)string(eg(sentance,words must be in quotes "hello",'maham')),3)(decimals(0.7,7.9,66.89..))
#4)boolean(True,False), T and F must be capital, 5)None (where we don't want to store any value in variable)
#boolen and none practice
age=23
old=False
a=None
print(type(old))
print(type(a))
part4="keywords"
#keywords are reserved words in python.you cannot use these variable as a name of your variable.e.g(and,None,True,False,if,else,import)
#its case sensitive language .you have to be careful while using lower or uper case.
a=2
b=3
sum=a+b #(arithematic operator)
print(a-b)
print(a*b)
print(a/b)
print(sum)#this is my program
part5="comments" #comments always define what we are doing in code.it define code.it just comment its not give output.
part6="operators"
#operands for example a and b is operand and + is operator
ar="arithematic used Math operation"
print(a%b)#by this we are finding reminder.module
print(a**b)#power operator we are calculating a^b.
br= "relational comparioson"#==,!=,<,>=,<=
x=50
y=20
print(x==y)#in these operators you may receive value true or false.means what it is saying may be true or false
print(a!=b)
print(a>=b)
print(a>b)
cr="assignment operator"#(=,+=,-=,*=,/=,%=,**=)
num=10 #num=num+10
num+=10
print(num)
#now we can write it in short by using assignment operator.its a short form 
dr="logical operator"#(not,and,or)
a1=50
b1=20
print(not a>b)
print(not False)
print(not True)
val1=True
val2=True
print("ans operator:",val1 and val2)#and operator is only true if both value true if one false answer false
print("ans operator:",val1 or val2)#if one is true in or operator it return true if both false then it is false
#you  can also do in this way print("ans operator:",(a1==b1) or (a>b)) by this way we have used two operators at same time
part7="type conversion"#we used this only when we convert into floating  value its conversion variable.it done automatoically
a3="type casting"#their are two types of conversion.but this done manually.
j=2#integars
k=4.25#float now python add two different classes
sum= j+k #this done automatically because this operation done automatically.
print(sum)#here type conversion took place
i=int("2") #here we have used int  function before value so we can easily add then this type casting
l=6#integars
#here string cannot be added to integars.so here we do type casting
# so to do type casting we used some functions 
# 1)integars: we used,int(value) 2)float(value) 3)
#type casting only work if their is no otherwise not.
n=3.14
n=str(n)
print(type(n))#here we convert it into string
part8="input in python"#by this you put answer in terminal and get answer
o=input("enter your name")#when it comes enter your name in terminal the press enter it will show you print result.
print("welcome", o)
#try it on age
e=input("enter your age:")
print("my age is:",e) #input statement result is always string let me show you in next step.
v1=input("enter some value")
print(type(v1),v1)#so input result is always string
#now do here type casting 
v2=int(input("enter"))
print(type(v2),v2)#here we have used type casting and convert it into integer.
part9="practice"
#first question:write a program to input 2 numbers and print their sum
first=int(input("enter first:"))
second=int(input("enter second:"))
print("sum:" , first+second)
#second question: Wrap to input side of a square and print its area
sqside=int(input("enter square side"))
print("area:", sqside * sqside)
#third question: WAP to input 2 floating point numbers and print their average
x= float(input("x first:"))
z= float(input("z second:"))
print("average:", (x+z)/2)
#WAPto input 2 int numbers ,io and eo. print True if io is greater than or equal to eo.if not print False
io=int(input("first integar"))
eo=int(input("second integar"))
print(io>=eo)








