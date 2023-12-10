"""
Enquries:
"""

#Create a function that has a multiple choice question
def test():
    print("Let's test your programming knowledge.")
    # write your code here
    question = ("What is Lambda in Python?")
    print(question)
    print("1. A keyword in Python for defining the anonymous fuunction.\n")
    print("2. A Placeholder.\n")
    print("3. An argument.\n")
    print("4. Non of the above.\n")
    answer = int(input())
    if answer == 1:
        print("Congratulations, have a nice day!")
    else:
        print("Please, try again.")

#Call the function
test()  #Correct answer is choice number 1.