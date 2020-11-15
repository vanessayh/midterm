from textblob import TextBlob #This section will import the textblob from the Python Library 

inpt = input("Please type out a statement:") # The user will insert a statement when asked

text = TextBlob(inpt) #TextBlob is used for input

x = text.sentiment.polarity #Checking the sentence for its polarity (neutral, negative, positive)

def my_function():  #Displaying comprehension of functions and doctrings
    """This is my display of a function and a docstring""" 
    return None 

print("using__doc__:")
print(my_function.__doc__) #This is where the docstring feature is used

#This is the else if loop for the statement

if x < 0:
    print("The statement is negative")
else if x > 0 and x <= 1:
    print("The statement is positive")
else 
    print("This statement is neutral")

