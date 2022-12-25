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

varAvg = 0
listStdIndex = []
for var in Student_Database:
 listStdIndex += [Student_Database[var]]

listSortedStd = (sorted(listStdIndex))


listTopHalf = []
listBottomHalf=[]

for var in range (0,len(listSortedStd)//2):
    listTopHalf += [listSortedStd[var]]
    listBottomHalf += [listSortedStd[0-(var+1)]]


listGroupSum = []
varTotal = 0

Group_Database = {}
for var in range(0,(len(listTopHalf)//2)):
    varTempList = [listTopHalf[var],listTopHalf[-var],listBottomHalf[var],listBottomHalf[-(var)]]
    listGroupSum+=[(listTopHalf[var]+listTopHalf[-var]+listBottomHalf[var]+listBottomHalf[-(var)])]
    varTotal += (listTopHalf[var]+listTopHalf[-var]+listBottomHalf[var]+listBottomHalf[-(var)])
    varGrpName = "Group" + str(var+1)
    Group_Database.update({varGrpName:varTempList})
print(Group_Database)

varAvg = varTotal/len(listGroupSum)
listVariance = []
varTemp = 0
for num in range (0,(2*len(listGroupSum)+1)):
    listVariance+=[0]
for num in listGroupSum:
    varTemp = int(num-varAvg)
    listVariance[len(listGroupSum)+varTemp]+=1

#print("\n\n\n\n\n\n",listVariance)

listX = []
listY = listVariance
listZ = []
varCount = -(len(listGroupSum))
varSum = 0

for num in range(0,(2*(len(listGroupSum)))+1):
    listX+=[varCount]
    varCount+=1
#for num in listY:
#    varSum+=num



print("\n\n\n\n\n\n",listX)
print("\n",listY)
graphix.plot(listX,listY)



graphix.ylabel("Number of Groups")
graphix.xlabel("Standard Deviation")
graphix.show()
