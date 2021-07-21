# The fourth assignment involves writing a Python program to compute the average quiz grade
# for a group of five students. Your program should include a list of five names.
# Using a for loop, it should successively prompt the user for the quiz grade for
# each of the five students. Each prompt should include the name of the student
# whose quiz grade is to be input. It should compute and display the average of
# those five grades and the highest grade. You should decide on the names of the five students.

#does the avg calculation for the grades
def Average(avggrade):
    return sum(avggrade) / len(avggrade)
#arrays ill need later in the program. Theyre currently blank
num_array = list()
avggrade = list()
#inputs the number of students in the class
Students = input("Enter how many Students you want:")

# runs untill the amount of students are inputed
for i in range(int(Students)):
    s = input("Enter Students name: ")
    print("\nPlease Enter", s, "'s")
    n = input("Grade: ")
    #adds the student and their grade together
    StudAndGrd = str(s) + " :" + str(n)
    #adds into array
    num_array.append(StudAndGrd)
    #adds avg grade into array
    avggrade.append(int(n))
    #uses functions to get avg
    average = Average(avggrade)
    #uses max to get the highest grade
    highest = max(avggrade)
    #prints
print("Students of the class with their grades \n", num_array)
print("The average grade is", average)
print("The best grade is", highest)
