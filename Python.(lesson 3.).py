lesson3="Dictionaries"
fr1="how to create" #dictionaries are used to store data values in key:value pairs
info={"key":"value",
      "name" : "maham",#this is the way to create dictionary
      "learning" : "coding",
      "age": 3,
       "boolean" : True,
       "subjects" : ["python","c++","java"], 
       "paper": ("English","urdu","maths")
      }
print(info)#dictionaries are unorder ,mutable(change),don"t create duplicate keys

print(info["name"])#you can also get it separetly
print(info["learning"])
print(info["subjects"])

info["name"]="Maham Arshad"#here we can replace
info["surname"]="Ghouri" #you can also add new value in it
print(info)
#empty dictionary
nul_dic={}#you can also create nul dictionary or empty dictionary  in which you can later on added value
nul_dic["surnam"]="Ghouri"
nul_dic["name"]="maham"
nul_dic["father"]="arshad"
print(nul_dic)
fr2="nested" 
student={
    "name":"maham",
    "age": 26,
    "gender": "female", #in this dictionary we have created another dictionary.this is nesting
    "subjects":{
        "phy":88,
        "maths": 99,
        "eng":78
    }

}
print(student) #nested dictionary
print(student["subjects"])
print(student["subjects"]["eng"]) #by this we can finds information within dictionary
fr3="methods"
#1) myDict.keys() returns all keys
print(student.keys())#here we finds keys
print(list(student.keys()))#here we convert it into list
print(len(student))#here we find out length
#2)myDict.values() return all values
print(student.values())
#3)myDict.items() return all (key,val) pairs as tuples
print(student.items())
#4)myDict.get("key") return the key according to value
print(student.get("name")) #its protect us from error
#5)myDict.update(newDict) insert the specified items to the dictionaries
student.update({"city":"Delhi"})
print(student)
fr4="set"#set is a collection of underscore items, or immutable or unique.set mutable but element immumtable
#lists and dictionaries never store in set
collection={1,2,3,4 ,"world"} #set is unorder
print(collection)
print(type(collection))#set ignore duplicate values means if (1,1, or any word came two timees it print one
#print empty set 
#empty set is alawys created first before we write set
emp=set() 
#methods
#1)set.add(el) #add an element
emp.add(45)
print(emp)
#2)set.remove(el) #removes the elem an
collection.remove("world")
print(collection)
#3)set.clear()empties the set
#collection.clear()

#4)set.pop() removes a random value
print(collection.pop())
#5)set.union(set2)
set1={1,2,3,4}
set2={"life","world"}
print ( set1.union(set2))
#6)set.intersection(set2)
print(set1.intersection(set2))

ab="practice"
#q1: creaate dictionary
dict5= {
    "table" : "a piece of furniture",
    "cat" : "a small animal"
}
print(dict5)
#q2:classes count for subject
listSub={"python","java","c++","javascript","python","java","python","java","c++","c"}
print(len(listSub))