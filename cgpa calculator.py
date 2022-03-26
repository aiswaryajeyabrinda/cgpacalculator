#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#cgpa calculator
def cgpaCalculator():
    TotalScore = 0
    obtainedGrade = 0
    numberOfSem = int(input("Enter number of semester: "))
    print()
    for i in range(numberOfSem):
        credits = int(input("enter course credits: "))
        score = int(input("enter your score"))
        print()
        TotalScore += credits* 5
        if(score >= 70):
            grade = 5
        elif(score < 70 and score >= 60):
            grade = 4
        elif(score < 60 and score >= 50):
            grade = 3
        elif(score < 50 and score >= 45):
            grade = 2
        elif(score < 45 and score >= 40):
            grade = 1
        else:
            grade = 0
            obtainedGrade += credits*grade
            cgpa = float((obtainedGrade/TotalScore)*5)
            print("Your cgpa is" + str(cgpa))
cgpaCalculator()

