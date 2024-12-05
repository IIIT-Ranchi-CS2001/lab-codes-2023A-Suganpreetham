Name=str(input("Enter your name: "))
Roll=int(input("Enter your Roll number: "))
Marks=int(input("Enter your marks in mathematics: "))
if(Marks<50):
    Grade=0
    Remarks="FAIL"
else :
    if(Marks<60):
        Grade=6
        Remarks="PASS"
    else:
        if(Marks<70):
            Grade=7
            Remarks="AVERAGE"
        else:
            if(Marks<80):
                Grade=8
                Remarks="GOOD"
            else:
                if(Marks<90):
                    Grade=9
                    Remarks="VERY GOOD"
                else:
                    if(Marks<=100):
                        Grade=10
                        Remarks="OUTSTANDING"
print("Name:",Name)
print("Roll Number:",Roll)
print("Marks:",Marks)
print("Grade Point:",Grade)
print("Remarks:",Remarks)