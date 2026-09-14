print ("================")
print ("welcome here")
print ("My first post!")
print ("============")

# git add, git commit activity 1, -m option is comment line for commit

username = "cool_creator"
bio = "Fun Blogger"
followers = 100

print ("Username:" , username)
print ( "Bio :", bio)
print ("followers :" , followers) 

# git diff, activity 2, git diff shows the new difference of the current code

followers +=50
print("Day 1:", followers)

followers +=20
print("Day 2:", followers)

followers -=10
print("Day 3:", followers)

#+= is the python shortcut function for adding to variable value
# Activity 3

username = input("Enter username :")
age = int(input ( "Enter age: "))
category = input ("Enter Content Category: ")

print ("\nInstagram profile")
print("==============")
print("Username: ", username)
print("Age: " , age)
print("Category:", category)

#Introduction to user sided input being run with input() function
# Activity 4

#call of input function to be int with int() function

if age>40 and category == "fun":
    print ("you are old what is fun for you")

