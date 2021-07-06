print ("Welcome to Grade Calculator")

a = input("Please enter your name: ")
x = int(input("Please enter your Homework(/25) score: "))
y = int(input("Please enter your Assessment(/50) score: "))
z = int(input("Please enter your Final Exam(/100) score: "))

s = (x + y + z)

calculation = (s/175)*100

def grade(calculation):
    if calculation <= 30:
        return("Your Grade is E.")
    elif calculation <= 50:
        return("Your Grade is D.")
    elif calculation <= 70:
        return("Your Grade is C.")    
    elif calculation <= 90:
        return("Your Grade is B.")
    elif calculation <= 100:
        return("Your Grade is A.")

print(a, "your score is:", s ,"out of 175. Your percentage is", calculation, grade(calculation))