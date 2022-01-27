# Created a function to write an input to a file. 
def writeToFile():
    filepath = input("Please enter the filepath: ")
    info = input("Please enter the info you wish to append: ")
    # Start of error handling
    # Only defined the error, because there isn't much that can go wrong (str).
    try:
        fileObject = open(filepath, 'a')
        fileObject.write("\n" + info)
        fileObject.close()
        print()
        print("operation completed successfully")
    except Exception as e:
        print()
        print(" *** ERROR HAS OCCURRED *** ")
        print("Error Type:", type(e))
        print("Error:", e)
        print("Error Arguments:", e.args)
        

# Created a function to read the contents of a text file.
def readToTextFile():
    filepath = input("Please enter the filepath: ")
    # Start of error handling
    # Only defined the error, because there isn't much that can go wrong (str).
    try:
        fileObject = open(filepath, 'r')
        text = fileObject.read()
        fileObject.close()
        print(text)
        print()
        print("operation completed successfully")
    except Exception as e:
        print()
        print(" *** ERROR HAS OCCURRED *** ")
        print("Error Type:", type(e))
        print("Error:", e)
        print("Error Arguments:", e.args)
        

# Created a function to read line by line the contents of a text file.
def readTextFileAsList():
    filepath = input("Please enter the filepath: ")
    # Start of error handling
    # Only defined the error, because there isn't much that can go wrong (str).
    try:
        fileObject = open(filepath, 'r')
        line = fileObject.readline()
        while(line != ""):
            print(line)
            line = fileObject.readline()
        fileObject.close()
        print()
        print("operation completed successfully")
    except Exception as e:
        print()
        print(" *** ERROR HAS OCCURRED *** ")
        print("Error Type:", type(e))
        print("Error:", e)
        print("Error Arguments:", e.args)
        
        

# Start of the main program
print()
print("**********************************")
print("Welcome to the Python text editor!")
print("**********************************")
print()

# Defining the loop condition
# Considered using try and except, but my orginial loop works on (str).
condition = "y"

while condition == "y":
    print("Please choose one of the following options: ")
    print()
    print(" 1.) Append lines to a file.")
    print(" 2.) Read a text file.")
    print(" 3.) Read a text file, line by line.")
    print()
    choice = input("Choice: ")
    if choice == "1":
        print()
        writeToFile()
        print()
    elif choice == "2":
        print()
        readToTextFile()
        print()
    elif choice == "3":
        print()
        readTextFileAsList()
        print()
    else:
        print()
        print("*** invalid entry ***")
        print()

    print()
    condition = input("Press 'y' to continue, anything else will exit?: ")
    











    


    
    
