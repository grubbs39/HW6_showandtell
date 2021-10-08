import HW5_3_1

student_info = {
    "Reagan" : "rebradshaw835",
    "Ryley" : "rbarber894",
    "Peyton" : "pstott885",
    "Tyrese" : "tmayo945",
    "Caius" : "ccharlton329"
}

print("Enter the users ID or name: ")
userChoice = input()

try:
    if userChoice == "0":
        name = input()
        result = HW5_3_1.find_ID(name, student_info)
    else:
        ID = input()
        result = HW5_3_1.find_name(ID, student_info)
    print(result)
except HW5_3_1.StudentInfoError as excpt:
    print(excpt)
