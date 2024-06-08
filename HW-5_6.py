types_of_people = 10 #Creating types of people
x = f"There are {types_of_people} types of people." #Importing types of people

binary = "binary" #Creating text "binary" for use
do_not = "don't" #Creating text "don't" for use
y = f"Those who know {binary} and those who {do_not}." #Importing binary and do not

print(x) #Printing first text
print(y) #Printing second text

print(f"I said: {x}") #Printing text importing x
print(f"I also said: '{y}'") #Printing text importing y

hilarious = False #Creating the value for placeholder
joke_evaluation = "Isn't that joke so funny?! {}" #Creating a placeholder inside the text

print(joke_evaluation.format(hilarious)) #Formatting the calue and inserting it inside the text

w = "This is the left side of..." #Creating text
e = "a string with a right side." #Creating another text

print(w + e) #Concatenating texts
