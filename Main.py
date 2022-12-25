def Logic():
    # Considering 80 participants in Batch 01
    # Getting to ratio 20,40,20 for three categories of students: Beginners, Morderates and Advanced
    # Scaling the situation to 10x smaller for demonstration purposes
    #Creating a sample List
    import random
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
    print(listStdIndex,"\n\n")
    listSortedStd = (sorted(listStdIndex))
    print(listSortedStd)

    listTopHalf = []
    listBottomHalf=[]

    for var in range (0,len(listSortedStd)//2):
        listTopHalf += [listSortedStd[var]]
        listBottomHalf += [listSortedStd[0-(var+1)]]

    print(sorted(listTopHalf),"\n")
    print(sorted(listBottomHalf))

    Group_Database = {}
    for var in range(0,(len(listTopHalf)//2)):
        varTempList = [listTopHalf[var],listTopHalf[-var],listBottomHalf[var],listBottomHalf[-(var)]]
        print(listTopHalf[var]+listTopHalf[-var]+listBottomHalf[var]+listBottomHalf[-(var)])
        varGrpName = "Group" + str(var+1)
        Group_Database.update({varGrpName:varTempList})
    print(Group_Database)

    Student_Database2 = Student_Database.copy()
    #print(Student_Database2)
    Group_Database2 = Group_Database.copy()

    '''for x in Group_Database:
        for var in Student_Database2:
            for y in range(0,4):
                 if Student_Database2.get(var) == Group_Database2.get(x)[y]:
                     Student_Database2.update({var:11})
                     Group_Database2[x][y] = var

    print(Student_Database2)
    print(Group_Database2)'''

def LogicPyPlot():
    # Considering 80 participants in Batch 01
    # Getting to ratio 20,40,20 for three categories of students: Beginners, Morderates and Advanced
    # Scaling the situation to 10x smaller for demonstration purposes
    #Creating a sample List
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
    #print(listStdIndex,"\n\n")
    listSortedStd = (sorted(listStdIndex))
    #print(listSortedStd)

    listTopHalf = []
    listBottomHalf=[]

    for var in range (0,len(listSortedStd)//2):
        listTopHalf += [listSortedStd[var]]
        listBottomHalf += [listSortedStd[0-(var+1)]]

    #print(sorted(listTopHalf),"\n")
    #print(sorted(listBottomHalf))

    Group_Database = {}
    for var in range(0,(len(listTopHalf)//2)):
        varTempList = [listTopHalf[var],listTopHalf[-var],listBottomHalf[var],listBottomHalf[-(var)]]
        #print(listTopHalf[var]+listTopHalf[-var]+listBottomHalf[var]+listBottomHalf[-(var)])
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

def HypothesisRandomisation():
    Student_Database = {}
    import random
    varStdQty = int(input("Enter number of Students >>"))+1
    for var in range(1,varStdQty):
        varStdID = "Student" + str(var)
        Student_Database.update({varStdID:random.randint(0,10)})
    print(Student_Database,"\n\n")

    randDict = {}
    for i in range(0,20):
        randDict.update({i+1:[]})

    print(randDict,"\n\n")
    x = 1
    for stdID in Student_Database:
        x = 1
        while x!=0:
            y=random.randint(1,20)
            if len(randDict.get(y))<4:
                randDict.update({y:randDict.get(y)+[stdID]})
                x = 0
    print(randDict)

def HypothesisFiltering():
    Student_Database = {}
    import random
    varStdQty = int(input("Enter number of Students >>"))+1
    for var in range(1,varStdQty):
        varStdID = "Student" + str(var)
        Student_Database.update({varStdID:random.randint(0,10)})
    print(Student_Database,"\n\n")

    randDict = {}
    for i in range(0,20):
        randDict.update({i+1:[]})

    print(randDict,"\n\n")
    x = 1
    for stdID in Student_Database:
        x = 1
        while x!=0:
            y=random.randint(1,20)
            if len(randDict.get(y))<4:
                randDict.update({y:randDict.get(y)+[stdID]})
                x = 0
    print(randDict,"\n\n")

    sumDict = {}
    sum = 0
    for n in range(1,21):
        varTemp = randDict.get(n)
        #print(varTemp)
        for z in varTemp:
            sum+=Student_Database.get(z)
        sumDict.update({n:sum})
        sum = 0
    print(sumDict)

def HypothesisExperimentation():
    #Code built for Data Entry Phase of hypothesis


    Student_Database={}
    varDivisor = int(input("Enter the total marks for assignments  >>"))
    varStdQty = int(input("Enter No. of Students >>"))
    for i in range(0,varStdQty):
        StdID = i+1
        AssignmentScore = (int(input("\n\nEnter Assginment Score >>"))/varDivisor)*10
        StarRating = (int(input("Enter Start rating >>")))*2
        MidSemMarks = (int(input("Enter Mid Sem Marks >>")))/10
        StdAvg = int((AssignmentScore+StarRating+MidSemMarks)/3)
        Student_Database.update({"Std "+str(StdID):StdAvg})
    print("\n\n\n\n",Student_Database)

def HypothesisRandomisationB():
    Student_Database = {}
    import random
    print("\n\nPlease Enter 80 below for perfect results (as 80 was considered while designing the code, it is easily possible to make it even more generalized after minor tweaks)\n\n")
    varStdQty = int(input("Enter number of Students (80) >>"))+1
    for var in range(1,varStdQty):
        varStdID = "Student" + str(var)
        Student_Database.update({varStdID:random.randint(0,10)})
    print("\n\n\n The randomly generated data of 80 students >>\n\n",Student_Database,"\n\n")

    randDict = {}
    valDict = {}
    groupSumDict = {}
    for i in range(0,20):
        randDict.update({i+1:[]})
        valDict.update({i+1:[]})

    #print(randDict,"\n\n")
    x = 1
    for stdID in Student_Database:
        x = 1
        while x!=0:
            y=random.randint(1,20)
            if len(randDict.get(y))<4:
                randDict.update({y:randDict.get(y)+[stdID]})
                valDict.update({y:valDict.get(y)+[Student_Database.get(stdID)]})
                x = 0
    print("\n\n\nThe data made by randomly distributing students into 20 groups >>\n\n",randDict)
    #newDict = randDict.copy()
    #print(newDict)
    #for x in randDict:
    #    for y in randDict.get(x):
    #        for z in Student_Database:
    #            if z == y:
    #                newDict.get(x).remove(z)
    #                newDict.get(x).append(Student_Database.get(z))
    #            else:
    #                pass
    #print(newDict)

    print("\n\n\nThe groupwise scores of rating for each student >>\n\n", valDict)
    varCumilate = 0
    for x in valDict:
        for y in valDict.get(x):
            varCumilate += y
        groupSumDict.update({x:varCumilate})
        varCumilate = 0

    print("\n\n\nThe cumilative scores of ratings for Groups >>\n\n",groupSumDict)

    varTotal = 0
    for X in groupSumDict:
        varTotal += groupSumDict.get(X)
    varAvg = varTotal/20

    print("\n\n\nAverage cumilative score based from all groups is : ",varAvg,"\n\n\n\n")

def HRBGraphPlot():
    Student_Database = {}
    import random
    print("\n\nPlease Enter 80 below for perfect results (as 80 was considered while designing the code, it is easily possible to make it even more generalized after minor tweaks)\n\n")
    varStdQty = int(input("Enter number of Students (80) >>"))+1
    for var in range(1,varStdQty):
        varStdID = "Student" + str(var)
        Student_Database.update({varStdID:random.randint(0,10)})
    #print("\n\n\n The randomly generated data of 80 students >>\n\n",Student_Database,"\n\n")
    randDict = {}
    valDict = {}
    groupSumDict = {}
    for i in range(0,20):
        randDict.update({i+1:[]})
        valDict.update({i+1:[]})
    x = 1
    for stdID in Student_Database:
        x = 1
        while x!=0:
            y=random.randint(1,20)
            if len(randDict.get(y))<4:
                randDict.update({y:randDict.get(y)+[stdID]})
                valDict.update({y:valDict.get(y)+[Student_Database.get(stdID)]})
                x = 0
    #print("\n\n\nThe data made by randomly distributing students into 20 groups >>\n\n",randDict)
    #print("\n\n\nThe groupwise scores of rating for each student >>\n\n", valDict)
    varCumilate = 0
    for x in valDict:
        for y in valDict.get(x):
            varCumilate += y
        groupSumDict.update({x:varCumilate})
        varCumilate = 0
    #print("\n\n\nThe cumilative scores of ratings for Groups >>\n\n",groupSumDict)
    varTotal = 0
    for X in groupSumDict:
        varTotal += groupSumDict.get(X)
    varAvg = varTotal/20
    #print("\n\n\nAverage cumilative score based from all groups is : ",varAvg,"\n\n\n\n")

    # THE GRAPH PLOTTING PART STARTS HERE ; Code again continued by Yashwardhan Dixit :)
    import matplotlib.pyplot as graphix
    listGroupNum = []
    listGroupSum = []
    listAvg = []
    listUpThreshold = []
    listBotThreshold = []
    for n in groupSumDict:
         listGroupSum += [groupSumDict.get(n)]
    #print(listGroupSum)
    for num in range(0,20):
        listGroupNum += [num+1]
        listAvg += [varAvg]
    #    listUpThreshold += [varAvg+1.5]
    #    listBotThreshold += [varAvg-1.5]
    graphix.plot(listGroupNum,listGroupSum)
    graphix.plot(listGroupNum,listAvg)
    #graphix.plot(listGroupNum,listUpThreshold)
    #graphix.plot(listGroupNum,listBotThreshold)
    graphix.ylabel("Cummilative Rating")
    graphix.xlabel("Group Number")
    graphix.show()

def HRBVariancePlot():
    Student_Database = {}
    import random
    print("\n\nPlease Enter 80 below for perfect results (as 80 was considered while designing the code, it is easily possible to make it even more generalized after minor tweaks)\n\n")
    varStdQty = int(input("Enter number of Students (80) >>"))+1
    for var in range(1,varStdQty):
        varStdID = "Student" + str(var)
        Student_Database.update({varStdID:random.randint(0,10)})
    #print("\n\n\n The randomly generated data of 80 students >>\n\n",Student_Database,"\n\n")
    randDict = {}
    valDict = {}
    groupSumDict = {}
    for i in range(0,20):
        randDict.update({i+1:[]})
        valDict.update({i+1:[]})
    x = 1
    for stdID in Student_Database:
        x = 1
        while x!=0:
            y=random.randint(1,20)
            if len(randDict.get(y))<4:
                randDict.update({y:randDict.get(y)+[stdID]})
                valDict.update({y:valDict.get(y)+[Student_Database.get(stdID)]})
                x = 0
    #print("\n\n\nThe data made by randomly distributing students into 20 groups >>\n\n",randDict)
    #print("\n\n\nThe groupwise scores of rating for each student >>\n\n", valDict)
    varCumilate = 0
    for x in valDict:
        for y in valDict.get(x):
            varCumilate += y
        groupSumDict.update({x:varCumilate})
        varCumilate = 0
    #print("\n\n\nThe cumilative scores of ratings for Groups >>\n\n",groupSumDict)
    varTotal = 0
    for X in groupSumDict:
        varTotal += groupSumDict.get(X)
    varAvg = varTotal/20
    #print("\n\n\nAverage cumilative score based from all groups is : ",varAvg,"\n\n\n\n")

    # THE GRAPH PLOTTING PART STARTS HERE ; Code again continued by Yashwardhan Dixit :)
    import matplotlib.pyplot as graphix
    listGroupNum = []
    listGroupSum = []
    listAvg = []
    listUpThreshold = []
    listBotThreshold = []
    for n in groupSumDict:
         listGroupSum += [groupSumDict.get(n)]
    #print(listGroupSum)
    for num in range(0,20):
        listGroupNum += [num+1]
        listAvg += [varAvg]
    #    listUpThreshold += [varAvg+1.5]
    #    listBotThreshold += [varAvg-1.5]
    '''graphix.plot(listGroupNum,listGroupSum)
    graphix.plot(listGroupNum,listAvg)
    #graphix.plot(listGroupNum,listUpThreshold)
    #graphix.plot(listGroupNum,listBotThreshold)
    graphix.ylabel("Cummilative Rating")
    graphix.xlabel("Group Number")
    graphix.show()'''
    listVariance = []
    for n in range(0,41):
        listVariance += [0] #21st element has to be Avg position (mid pos of bell curve)
    print(listVariance)
    varTemp = 0
    for n in range(1,21):
        varTemp = groupSumDict.get(n) - int(varAvg)
        listVariance[(21+varTemp)]+=1
    print(listVariance)
    listX = []
    varTemp = -20
    for n in range(0,41):
        listX+=[varTemp]
        varTemp+=1
    #print(listX)
    graphix.plot(listX,listVariance)
    graphix.show()

def HRBMLModule():
    #HypothesisRandomisation-B , ML Module, Documented version of HR-B_MLModule(Unreliable).py
    #Code by Yashwardhan Dixit and Chandan Dhamande, Saksham (plotting), Rajni  (input)



    # !! --- PART A: GENERATING RANDOM SEED GROUPS --- !!



    # Part A.1: Initialising Student Database
    Student_Database = {}
    import random
    print("\n\nPlease Enter 80 below for perfect results (as 80 was considered while designing the code, it is easily possible to make it even more generalized after minor tweaks)\n\n")
    varStdQty = int(input("Enter number of Students (80) >>"))+1
    for var in range(1,varStdQty):
        varStdID = "Student" + str(var)
        Student_Database.update({varStdID:random.randint(0,10)})



    # Part A.2: Generating random data in accordance to Student Database
    randDict = {}
    valDict = {}
    groupSumDict = {}
    for i in range(0,20):
        randDict.update({i+1:[]})
        valDict.update({i+1:[]})
    x = 1
    for stdID in Student_Database:
        x = 1
        while x!=0:
            y=random.randint(1,20)
            if len(randDict.get(y))<4:
                randDict.update({y:randDict.get(y)+[stdID]})
                valDict.update({y:valDict.get(y)+[Student_Database.get(stdID)]})
                x = 0



    # Part A.3: Generating Database of Gross Rating for all Groups
    varCumilate = 0
    for x in valDict:
        for y in valDict.get(x):
            varCumilate += y
        groupSumDict.update({x:varCumilate})
        varCumilate = 0



    # Part A.4: Using sumed up values for generating a databse that stores standard deviation from average rating
    varTotal = 0
    for X in groupSumDict:
        varTotal += groupSumDict.get(X)
    varAvg = varTotal/20



    # !! --- PART B: INITIALIZING GRAPHING REQUIREMENTS --- !!




    # Part B.1: Importing Necessary Libraries
    import matplotlib.pyplot as graphix
    listGroupNum = []
    listGroupSum = []
    listAvg = []
    listUpThreshold = []
    listBotThreshold = []
    for n in groupSumDict:
         listGroupSum += [groupSumDict.get(n)]



    # Part B.2: Generating Lists with Basic Plotting Data
    for num in range(0,20):
        listGroupNum += [num+1]
        listAvg += [varAvg]



    # !! --- PART C: FILTERING GROUPS (To be looped) --- !!



    # Part C.1: Calculating Individual Deviation values (Variances) for each group
    filteredGroupDict = randDict.copy()   #<---  To Be REMOVED LATER
    listVariance = []
    for n in range(0,41):
        listVariance += [0] #21st element has to be mid position
    print(listVariance)
    varTemp = 0
    VarianceDict = {}
    for n in range(1,21):
        varTemp = groupSumDict.get(n) - int(varAvg)
        VarianceDict.update({n:varTemp})
        listVariance[(21+varTemp)]+=1
    print(listVariance)
    listX = []
    varTemp = -20
    for n in range(0,41):
        listX+=[varTemp]
        varTemp+=1
    print(VarianceDict)



    # Part C.2: Selection and Rejection of Groups for sorting based upon deviation values
    FilterDict = {} #Dictionary of groups that will be considered for filtering in the current round
    listFilterGroups = [] # COllection of Cummilative ratings of all groups considered for filtering in current round
    varThres = int(input("Please enter Threshold Index >>")) # for range of +- X where X is threshold index
    for group in VarianceDict:
        if VarianceDict.get(group) <= -varThres or VarianceDict.get(group) >= varThres:
            FilterDict.update({group:VarianceDict.get(group)})
            listFilterGroups+=[VarianceDict.get(group)]



    # Part C.3: Selection and Rejection of Groups for filterUp category and filterLow category
    listFilterGroups = sorted(listFilterGroups)
    listFilterUp = []
    listFilterLow = []
    for var in range (0,len(listFilterGroups)//2):
        listFilterUp += [listFilterGroups[var]]
        listFilterLow += [listFilterGroups[0-(var+1)]]
    print(listFilterUp)
    print(listFilterLow)
    FilterUpDict = {}
    FilterLowDict = {}
    listFilterUpGroups = []
    listFilterLowGroups = []
    VarianceDictCopy = VarianceDict.copy()
    for y in listFilterUp:
        for group in VarianceDict:
            if y == VarianceDictCopy.get(group):
                FilterUpDict.update({group:y})
                listFilterUpGroups+=[group]
                VarianceDictCopy.pop(group)
    print("\nFilter Up Groups : \n",listFilterUpGroups)
    print(FilterUpDict)
    filterValDict = {} # Filter version of valDict (for Filter Up groups)
    for group in listFilterUpGroups:
        filterValDict.update({group:sorted(valDict.get(group))})
    print(filterValDict)
    filterStdValDict = {}
    for group in filterValDict:
        filterStdValDict.update({group:[]})
    Student_Database3 = Student_Database.copy()
    for group in filterValDict:
        for stdRating in filterValDict.get(group):
            for stdID in randDict.get(group):
                if stdRating == Student_Database3.get(stdID):
                    filterStdValDict[group]+=[stdID]
                    Student_Database3.pop(stdID)
    print(filterStdValDict)
    print("\n\n\n For Filter Low Groups")
    VarianceDictCopy = VarianceDict.copy()
    for y in listFilterLow:
        for group in VarianceDict:
            if y == VarianceDictCopy.get(group):
                FilterUpDict.update({group:y})
                listFilterLowGroups+=[group]
                VarianceDictCopy.pop(group)
    print("\nFilter Low Groups : \n",listFilterLowGroups)
    print(FilterLowDict)
    filterValDict2 = {} # Filter version of valDict (for Filter Low groups)
    for group in listFilterLowGroups:
        filterValDict2.update({group:sorted(valDict.get(group))})
    print(filterValDict2)
    filterStdValDict2 = {}
    for group in filterValDict2:
        filterStdValDict2.update({group:[]})
    Student_Database4 = Student_Database.copy()
    for group in filterValDict2:
        for stdRating in filterValDict2.get(group):
            for stdID in randDict.get(group):
                if stdRating == Student_Database4.get(stdID):
                    filterStdValDict2[group]+=[stdID]
                    Student_Database4.pop(stdID)
    print(filterStdValDict2)



    # Part C.4: Sorting students on the basis of previous results of selection categories
    varTempHi = 0
    varTempLo = 0
    varUpGroupNum = 0
    varLoGroupNum = 0
    for count in range(0,len(listFilterUp)):
        varTempHi = (filterStdValDict.get(listFilterUpGroups[0-(count+1)]))[-1] #Highest student of the current filter low group
        varTempLo = (filterStdValDict2.get(listFilterLowGroups[count]))[0] #Lowest student of the current filter up group
        varUpGroupNum = listFilterUpGroups[0-(count+1)]
        varLoGroupNum = listFilterLowGroups[count]
        filteredGroupDict[varUpGroupNum].remove(varTempHi)
        filteredGroupDict[varLoGroupNum].remove(varTempLo)
        filteredGroupDict[varUpGroupNum]+=[varTempLo]
        filteredGroupDict[varLoGroupNum]+=[varTempHi]

    # PART D coming soon (Graph plotting and data variation)
    # Code by Yashwardhan Dixit and Chandan Dhamande.

    # !!--- END OF CODE ---!! #

def HRBMLModuleLoop() :
    Student_Database = {}
    import random
    import matplotlib.pyplot as graphix
    print("\n\nPlease Enter 80 below for perfect results (as 80 was considered while designing the code, it is easily possible to make it even more generalized after minor tweaks)\n\n")
    varStdQty = int(input("Enter number of Students (80) >>"))+1
    for var in range(1,varStdQty):
        varStdID = "Student" + str(var)
        Student_Database.update({varStdID:random.randint(0,10)})

    randDict = {}
    valDict = {}
    groupSumDict = {}
    for i in range(0,20):
        randDict.update({i+1:[]})
        valDict.update({i+1:[]})
    x = 1
    for stdID in Student_Database:
        x = 1
        while x!=0:
            y=random.randint(1,20)
            if len(randDict.get(y))<4:
                randDict.update({y:randDict.get(y)+[stdID]})
                valDict.update({y:valDict.get(y)+[Student_Database.get(stdID)]})
                x = 0

    filteredGroupDict = randDict.copy()
    varAtmpt = int(input("\n\n Enter number of filter cycles to perform >>"))
    varThresVal = int(input("\n\n Threshold Value >>"))
    valDictCopy = valDict.copy()
    while (varAtmpt-1) >= 0:
        varCumilate = 0
        for x in valDict:
            for y in valDict.get(x):
                varCumilate += y
            groupSumDict.update({x:varCumilate})
            varCumilate = 0
        varTotal = 0
        groupSumDictCopy = groupSumDict.copy()
        for X in groupSumDict:
            varTotal += groupSumDict.get(X)
        varAvg = varTotal/20
        listGroupNum = []
        listGroupSum = []
        listAvg = []
        listUpThreshold = []
        listBotThreshold = []
        for n in groupSumDict:
             listGroupSum += [groupSumDict.get(n)]
        for num in range(0,20):
            listGroupNum += [num+1]
            listAvg += [varAvg]
        listVariance = []
        for n in range(0,41):
            listVariance += [0] #21st element has to be mid position
        print(listVariance)
        varTemp = 0
        VarianceDict = {}
        for n in range(1,21):
            varTemp = groupSumDict.get(n) - int(varAvg)
            VarianceDict.update({n:varTemp})
            listVariance[(21+varTemp)]+=1
        print(listVariance)
        listX = []
        varTemp = -20
        for n in range(0,41):
            listX+=[varTemp]
            varTemp+=1
        print(VarianceDict)
        FilterDict = {} #Dictionary of groups that will be considered for filtering in the current round
        listFilterGroups = [] # COllection of Cummilative ratings of all groups considered for filtering in current round
        varThres = varThresVal # for range of +- X where X is threshold index
        for group in VarianceDict:
            if VarianceDict.get(group) <= -varThres or VarianceDict.get(group) >= varThres:
                FilterDict.update({group:VarianceDict.get(group)})
                listFilterGroups+=[VarianceDict.get(group)]
        listFilterGroups = sorted(listFilterGroups)
        listFilterUp = []
        listFilterLow = []
        for var in range (0,len(listFilterGroups)//2):
            listFilterUp += [listFilterGroups[var]]
            listFilterLow += [listFilterGroups[0-(var+1)]]
        print(listFilterUp)
        print(listFilterLow)
        FilterUpDict = {}
        FilterLowDict = {}
        listFilterUpGroups = []
        listFilterLowGroups = []
        VarianceDictCopy = VarianceDict.copy()
        for y in listFilterUp:
            for group in VarianceDict:
                if y == VarianceDictCopy.get(group):
                    FilterUpDict.update({group:y})
                    listFilterUpGroups+=[group]
                    VarianceDictCopy.pop(group)
        print("\nFilter Up Groups : \n",listFilterUpGroups)
        print(FilterUpDict)
        filterValDict = {} # Filter version of valDict (for Filter Up groups)
        for group in listFilterUpGroups:
            filterValDict.update({group:sorted(valDict.get(group))})
        print(filterValDict)
        filterStdValDict = {}
        for group in filterValDict:
            filterStdValDict.update({group:[]})
        Student_Database3 = Student_Database.copy()
        for group in filterValDict:
            for stdRating in filterValDict.get(group):
                for stdID in randDict.get(group):
                    if stdRating == Student_Database3.get(stdID):
                        filterStdValDict[group]+=[stdID]
                        Student_Database3.pop(stdID)
        print(filterStdValDict)
        print("\n\n\n For Filter Low Groups")
        VarianceDictCopy = VarianceDict.copy()
        for y in listFilterLow:
            for group in VarianceDict:
                if y == VarianceDictCopy.get(group):
                    FilterUpDict.update({group:y})
                    listFilterLowGroups+=[group]
                    VarianceDictCopy.pop(group)
        print("\nFilter Low Groups : \n",listFilterLowGroups)
        print(FilterLowDict)
        filterValDict2 = {} # Filter version of valDict (for Filter Low groups)
        for group in listFilterLowGroups:
            filterValDict2.update({group:sorted(valDict.get(group))})
        print(filterValDict2)
        filterStdValDict2 = {}
        for group in filterValDict2:
            filterStdValDict2.update({group:[]})
        Student_Database4 = Student_Database.copy()
        for group in filterValDict2:
            for stdRating in filterValDict2.get(group):
                for stdID in randDict.get(group):
                    if stdRating == Student_Database4.get(stdID):
                        filterStdValDict2[group]+=[stdID]
                        Student_Database4.pop(stdID)
        print(filterStdValDict2)
        varTempHi = 0
        varTempLo = 0
        varUpGroupNum = 0
        varLoGroupNum = 0
        for count in range(0,len(listFilterUp)):
            varTempHi = (filterStdValDict.get(listFilterUpGroups[0-(count+1)]))[-1] #Highest student of the current filter low group
            varTempLo = (filterStdValDict2.get(listFilterLowGroups[count]))[0] #Lowest student of the current filter up group
            varUpGroupNum = listFilterUpGroups[0-(count+1)]
            varLoGroupNum = listFilterLowGroups[count]
            filteredGroupDict[varUpGroupNum].remove(varTempHi)
            filteredGroupDict[varLoGroupNum].remove(varTempLo)
            filteredGroupDict[varUpGroupNum]+=[varTempLo]
            filteredGroupDict[varLoGroupNum]+=[varTempHi]
        for varGroup in filteredGroupDict:
            valDict[varGroup] = []
            for stdID in filteredGroupDict.get(varGroup):
                valDict.update({varGroup:valDict.get(varGroup)+[Student_Database.get(stdID)]})
        print(valDict)
        #stBreak = input("\n\n\n\n\n\n\nDo you wanna continue? >>\n\n\n\n\n\n")
        varAtmpt -= 1
    listFilteredGroupSums = []
    varTemp = 0
    for Group in filteredGroupDict:
        varTemp=0
        for Std in filteredGroupDict.get(Group):
            pass
            varTemp += Student_Database.get(Std)
        listFilteredGroupSums+=[varTemp]
    listGroupSum = []
    for key in groupSumDictCopy:
        listGroupSum+=[groupSumDictCopy.get(key)]
    print("\n\n\n\n\n\n\n\n The Original List \n\n")
    print(listGroupSum)
    print("\n\n The Final List \n\n")
    print(listFilteredGroupSums)
    #print(Student_Database)

def GLBasic():
    # FIRST SANCTIONED PROGRAM FOR GREEDY LOGIC (GL)
    # Code By Yashwardhan Dixit and Chandan Dhamande
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

def GLBBellCurve():

    # Code By Yashwardhan Dixit and Chandan Dhamande
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

def ProgSkyline():
    import random
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    def make_data(numStd):
        listScr = []
        listGenLap = []
        listNum = []
        for num in range(0,numStd):
            varScr = random.randint(0,100)
            varGen = random.randint(0,100)
            varLap = random.randint(0,0)
            listScr+=[varScr]
            listNum+=[num]
            listGenLap+=[varGen+varLap]
        return pd.DataFrame({
            'ID' : listNum ,
            'SC' : (listScr) ,
            'GL' : (listGenLap)
        })
    def a_dominates_b(a, b, to_max, to_max2):

        n_better = 0
        if a[to_max] > b[to_max]:
            n_better+=1
        elif a[to_max] < b[to_max]:
            n_better-=1
        if a[to_max2] > b[to_max2]:
            n_better+=1
        elif a[to_max2] < b[to_max2]:
            n_better-=1
        if n_better > 0:
            return True
        return False





    Data = make_data(142)

    a = {'price': 120000, 'size': 390}
    b = {'price': 120000, 'size': 200}
    #print(a_dominates_b(a, b, to_max='price', to_max2='size'))
    #print(a['price'])

    def find_skyline_brute_force(df, to_max, to_max2):

        rows = df.to_dict(orient='index')

        skyline = set()

        for i in rows:

            dominated = False

            for j in rows:

                if i == j:
                    continue

                if a_dominates_b(rows[j], rows[i], to_max, to_max2):
                    dominated = True
                    break

            if not dominated:
                skyline.add(i)

        return pd.Series(df.index.isin(skyline), index=df.index)
    skyLine = find_skyline_brute_force(Data,to_max='SC',to_max2='GL')
    print(skyLine)
    x = []
    y = []

    for ind in Data.index:
        x += [(Data['GL'][ind])]
        y += [(Data['SC'][ind])]

    x2 = []
    y2 = []
    count = 0
    Tcount = 0
    for bool in skyLine:
        #print(bool)
        #print(count)
        if bool == True:
            Tcount+=1
            y2+=[y[count]]
            x2+=[x[count]]
        count+=1
    print("Tcount :",Tcount)
    for ind in skyLine.index:
        pass
    plt.rcParams['axes.facecolor'] = 'black'

    plt.scatter(x, y, s=np.pi*25, c='blue', alpha=0.5)
    plt.scatter(x2,y2,s=np.pi*25, c='red', alpha=0.5)
    plt.title("Sample Data")
    plt.show()

x = 1

while x!=0:
    print("This is the compendium of whole Diverse CLustering Project") # remember to put \n's after exec of any prog
    print("\n\nThe participants are: ")
    print("\tYashwardhan Dixit - 20190802138\n\tChandan Dhamande - 20190802117")
    print("\tRajni Gupta - 20190802012\n\tSaksham Agrawal - 20190802132")
    print("\n\n ============================================================== \n\n")
    print("Enter a number to run the desired program as a function >> \n")
    print("Logic.py ................................... 0")
    print("LogicPyPlot.py ............................. 1")
    print("HypotheticalRandomisation.py ............... 2")
    print("HypothesisFiltering.py ..................... 3")
    print("HypothesisExperimentation/py ............... 4")
    print("HypothesisRandomisation-B.py ............... 5")
    print("HR-B GraphPlot.py .......................... 6")
    print("HR-B VariancePlot .......................... 7")
    print("HR-B ML Module ............................. 8")
    print("HR-B ML Module Looped ...................... 9")
    print("Greedy Logic Basic ........................ 10")
    print("GL-B Bell Curve ........................... 11")
    print("Progressive Skyline ....................... 12")
    varProgChoice = int(input("\n\nEnter your choice here >>"))
    if varProgChoice == 13:
        x = 0
    if varProgChoice == 1:
        print("\n\n")
        Logic()
        print("\n\n")
    if varProgChoice == 2:
        print("\n\n")
        LogicPyPlot()
        print("\n\n")
    if varProgChoice == 7:
        print("\n\n")
        HRBVariancePlot()
        print("\n\n")
    if varProgChoice == 6:
        print("\n\n")
        HRBGraphPlot()
        print("\n\n")
    if varProgChoice == 8:
        print("\n\n")
        HRBMLModule()
        print("\n\n")
    if varProgChoice == 9:
        print("\n\n")
        HRBMLModuleLoop()
        print("\n\n")
    if varProgChoice == 3:
        print("\n\n")
        HypothesisFiltering()
        print("\n\n")
    if varProgChoice == 4:
        print("\n\n")
        HypothesisExperimentation()
        print("\n\n")
    if varProgChoice == 5:
        print("\n\n")
        HypothesisRandomisationB()
        print("\n\n")
    if varProgChoice == 10:
        print("\n\n")
        GLBasic()
        print("\n\n")
    if varProgChoice == 11:
        print("\n\n")
        GLBBellCurve()
        print("\n\n")
    if varProgChoice == 12:
        print("\n\n")
        ProgSkyline()
        print("\n\n")
