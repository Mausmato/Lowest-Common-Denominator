#math library
import math
#Fraction and input variables
int1=int(input("Type in an integer numerator: "))
int2=int(input("Type in an integer denominator: "))
#undefined fraction
if int2==0:
  print("The denominator cannot be 0, the fraction is undefined ")
  quit()
#gcd
gcd=math.gcd(int1,int2)
#simplifying
simp_1=int(int1/gcd)
simp_2=int(int2/gcd)
#simplified fraction printed
if simp_1==simp_2:
  print("The simplified fraction is",simp_1)  
#Switching the negative from the denominator to the numerator
elif simp_2 <0 and simp_1 >0:
  print("The simplified fraction is",simp_1*-1,"/",simp_2*-1)
#simplifying fraction denominator
elif simp_2==1:
  print("The simplified fraction is",simp_1)
#simplifing negative fraction denominator
elif simp_2==-1:
  print("The simplified fraction is",simp_1*-1)
#if the fraction has 2 negative integers
elif simp_1 <0 and simp_2 <0:
  print('The simplifyed fraction is ',simp_1*-1,"/",simp_2*-1,"!")
#if the fraction has one negative integer
else:
  print('The simplifyed fraction is ',simp_1,"/",simp_2,"!")




