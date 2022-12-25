# GL-B (Gen-Con Edition) Ver 2.0.1
# This is the Gender Constraint Version of GL-B
# Current Program Version 2.0.1
# VERSION LOG:
#  Version 2.0.1 --> 26 Oct 2019 --> Initialization ; Considering perfect 3:1 Male-Female Ratio

import random

#PART 01: Generating random database of 60 Male Students

dictMale = {}               # Initialization of Dictionary
for num in range(1,61):
    dictMale.update({'M_Std'+str(num):random.randint(0,10)})
print("Male Students Database :\n",dictMale)



#PART 02: Generating random database of 20 Female Students

dictFemale = {}
for num in range(1,41):
    dictFemale.update({'F_Std'+str(num):random.randint(0,10)})
print("\n\n\nFemale Students Database :\n",dictFemale)
