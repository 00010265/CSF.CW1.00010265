# To create lists we use  []
# To create tuples we use ()
# To create Dictionaries we use {}
# >>>>LISTS
datatypes=["Lists","Tuples", "Dictionaries"]

#Lists are ordered and indexed. We can call items from lists using their indices
print(datatypes[0]) #this will print out first item in the list which is "Lists"
print(datatypes[-1]) #negative index is used to count from the end. In this case, the program will print out last item "Dictionaries"
print(datatypes[1:2]) #Also we may use range to access several items from the list. In this case we call second and third items -"Tuples", "Dictionaries"

#Because lists are mutable, we may change their items
datatypes[1]= "sets" #This operation changes second item of initaial list from "Tupples" to "sets"
print(datatypes)
datatypes[1]=["sets","Tuples"] #here we replaced second item with two items
print(datatypes)

#we may also use range to change several items
listofnumbers=["1","2","3","4","5"]
listofnumbers[1:3]=["20","30"] 
print(listofnumbers) #here we chaged "2" and "3" to "20" and "30"

#Also, we can add one list to another with just + operator
num1=["1","2","3"]
num2=["4","5","6"]
num3=num1+num2
print(num3)# now the third list contains all items from first and second lists

#>>>TUPLES
""" Tuples are much like lists with slight difference - they are immutable, which mean the methods like appending and inserting will not work
with them."""
tuple1=("Amazon","Tesla","Microsoft")# this is the tuple and it cannot be changed

#However we can still address items inside tuples if we need just like we did with lists - through index number
print(tuple1[1])# we asked for the second number in the tupple and we get "Tesla"
#Just like in lists, we can use negative indexes and ranges
print(tuple1[-1])# Printing last item of the tuple
print(tuple1[:2]) #We set range till 3rd element, not including it
#I previously mentioned that tuples are immutable, but still there are ways to make some change.

subjects = ("CFS", "WebTech", "FunPro")
mylessons1 = list(subjects) #First we change the tuple into list
mylessons1.append("IMOB") #then append the list
subjects2 = tuple(mylessons1) #and finally convert the list back to tuple

#>>> Dictionaries
"""Dictionaries store data values in pairs: keys and values.
A dictionaries , unlike tuples and lists, are unordered and does not allow duplicates, and like lists, they are changable."""
myfavorites={
    "game": "Dota",
    "music": "rock",
    "film": "Watchmen"
}
print(myfavorites)

#We can access values inside dicts using keys
y= myfavorites["film"]
print("My favorite film is",y)

#>>> ADDITIONS

#When we want to add other list, then we may use extend method
listofcountries=["Uzbekistan","Russia"]
listofcountries2=["Turkmenistan", "Tajikistan"]
listofcountries.extend(listofcountries2)
print(listofcountries) #Now the content of second list of countriess was added at the end of fist list
#To note, good thing about extend method is that the items added does not necessarily need to be in list. We may add even tuples

#There is also a zip function that iterates, pairing items in them
grooms=("Begzod","Shahzod","Dilshod")
brides=("Shahnoza","Dulfuza","Malika")#there are two tuples
q=zip(grooms,brides)#now two tuples are zipped
print(tuple(q)) #here we can see new tuple printed out

#there are also an enumerate function that  adds counter to an iterable and returns it as an enumerate object
laptops = ['hp', 'acer', 'asus'] #there are a list of laptops
#we can use this little function below to enumarate these laptops
for i in enumerate(laptops):
  print(i)










