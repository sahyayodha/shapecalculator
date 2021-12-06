import math
pembatas="---------------------"
print(pembatas)
print("SHAPE CALCULATOR")
print("BY : NEOZA")
print(pembatas)

shape=str(input("Shape Type[Rectangle|Circle|Triangle|Trapesium] : "))
print(pembatas)

if shape=="Rectangle" or shape=="rectangle" : 
  lengthrectangle1=int(input("Rectangle Length 1 : "))
  lengthrectangle2=int(input("Rectangle Length 2 : "))
  lk=lengthrectangle1*lengthrectangle2
  print("Rectangle Area :", lk)
  print(pembatas)

elif shape=="Circle" or shape=="circle" : 
  diametercircle=int(input("Circle Diameter : "))
  radiuscircle=diametercircle/2
  calculationcircle=radiuscircle*radiuscircle
  phi=22/7
  ll=calculationcircle*phi
  print("Circle Area :", ll)
  print(pembatas)

elif shape=="Triangle" or shape=="triangle" :
  heighttriangle=int(input("Triangle Height : "))
  basetriangle=int(input("Triangle Base : "))
  calculationtriangle=1/2
  lt=heighttriangle*basetriangle*calculationtriangle
  print("Triangle Area:", lt)
  print(pembatas)

elif shape=="Trapesium" or shape=="trapesium" :
  lengthtrapesium1=int(input("Trapesium Length 1 : "))
  lengthtrapesium2=int(input("Trapesium Length 2 : "))
  heighttrapesium=int(input("Trapesium Height : "))
  calculationtrapesium=1/2
  calculateddiagonaltrapesium=lengthtrapesium1+lengthtrapesium2
  lm=calculationtrapesium*heighttrapesium*calculateddiagonaltrapesium
  print("Trapesium Area :", lm)
  print(pembatas)

elif shape=="amogus" :
  print("SUS")
  print(pembatas)

else :
  print("ERROR")
  print(pembatas)
