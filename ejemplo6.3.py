import pickle
from pathlib import Path

#create an empty dictionary
d = dict()

#ASk for file name to load dictionary from
file_name = input("Enter the file name with the data: ")

#Make sure that it exists
path = Path(file_name)
if path.is_file():
  # Open file in reading mode
  input_file = open(file_name, 'rb')
  d = pickle.load(input_file)
  #Close the file 
  input_file.close()
else:
  print("File doesn't exist, an empty dictionary has been created.")

#Check for values or add new ones
document_number = input("Enter an ID ")

if document_number in d: #Check wether it is on dict or not
  print ("Age of " + document_number + " is " + str(d[document_number]))
else: 
  age = input("ID doesn't exist in register. Enter an age: ")

  if age.isnumeric():

    num = int(age)
    d[document_number] = num 
    print("Added to the dictionary")

# Save dict on file and close
output_file = open(file_name, 'wb')
pickle.dump(d, output_file)
output_file.close()
