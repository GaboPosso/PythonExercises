# Program to ask a subject grade and evaluates if the student has passed
gradeIn = int(input("Enter grade: "))

if gradeIn < 5:
    grade = 'Suspense'
else:
    grade = "Approved"

print("Grade: {}".format(grade))

# If not only evaluates a boolean, it also evaluates if a variable contains info

variable = 19

if variable:
    print("Contains information")
else:
    print("Doesn't contain information")

# Program that asks an age and evaluates if the user is an adult or not.

age = int(input("Enter age: "))

if age < 18:
    print("You can't pass")
elif age > 100:
    print("Wrong age")
else:
    print("Go on!")

# Program that asks for a grade and  evaluates the possible student's score.

grade = int(input("Enter grade: "))

if grade < 5:
    print("Suspense")
elif grade < 7:
    print("Approved")
elif grade < 9:
    print("Notable")
else:
    print("Outstanding")

# Abbreviated IF
n_num1 = 5
n_num2 = 10
if n_num1 > n_num2: print(n_num1, " es mayor que ", n_num2)

#Abbrevaited IF...ELSE
a = 2
b = 330
print ("A") if a > b else print("B")

# It can concatenate comparison operators

age = 117
if 0 < age < 100: # It's like: if age>0 and age<100
    print("Right age")
else:
    print("Wrong age")

# Another example about concatenated comparison operators

chairmanSalary = int(input("Enter chairman salary: "))

directorSalary = int(input("Enter director salary: "))

bossSalary = int(input("Enter boss salary: "))

operatorSalary = int(input("Enter operator salary: "))

if operatorSalary > bossSalary > directorSalary > chairmanSalary:
    print("Everything is fine")
else:
    print("Something is wrong")

# AND - OR operators

distance = int(input("Enter distance: "))
numBrothers = int(input("Enter number of brothers: "))
meanGrade = int(input("Enter average age: "))

if distance > 20 or numBrothers < 2 or meanGrade <= 5:
    print("You're not a candidate for the studentship. ")
else:
    print("You're a candidate for the studentship. ")

# IN operator

option = input("Choose an option: option1, option2, option3, option4: ")

setLowercase = option.lower()

if setLowercase in ("option1, option2, option3, option4"):
    print("Valid option: " + setLowercase)
else:
    print("Invalid option " + setLowercase)