# FIRST SANCTIONED PROGRAM FOR GREEDY LOGIC (GL)
# Code By Yashwardhan Dixit ;)
# Scaling the situation to 10x smaller for demonstration purposes

import random
import matplotlib.pyplot as graphix
Student_Database = {}
#To create a random student database
varStdQty = int(input("Enter number of Students >>"))+1
for var in range(1,varStdQty):
    varStdID = "Student" + str(var)
    Student_Database.update({varStdID:random.randint(0,10)})
print(Student_Database,"\n\n")


listStdIndex = []
for var in Student_Database:
 listStdIndex += [Student_Database[var]]

listSortedStd = (sorted(listStdIndex))


listTopHalf = []
listBottomHalf=[]

for var in range (0,len(listSortedStd)//2):
    listTopHalf += [listSortedStd[var]]
    listBottomHalf += [listSortedStd[0-(var+1)]]



Group_Database = {}
for var in range(0,(len(listTopHalf)//2)):
    varTempList = [listTopHalf[var],listTopHalf[-var],listBottomHalf[var],listBottomHalf[-(var)]]
    varGrpName = "Group" + str(var+1)
    Group_Database.update({varGrpName:varTempList})
print(Group_Database)

listX = []
listY = []
listZ = []
varCount = 1
varSum = 0
varAvg = 0
for var in Group_Database:
    for num in Group_Database[var]:
        varSum+=num
    listY+=[varSum]
    listX+=[varCount]
    varSum = 0
    varCount+=1
for num in listY:
    varSum+=num
varAvg = varSum/len(listY)
listTop = []
listBot = []
for num in range(0,len(listX)):
    listZ+=[varAvg]
    listTop += [40]
    listBot += [0]
graphix.plot(listX,listY)
graphix.plot(listX,listZ)
graphix.plot(listX,listTop)
graphix.plot(listX,listBot)

graphix.ylabel("Gross Rating (Group)")
graphix.xlabel("Group Number")
graphix.show()
