print("Water Jug Problem")
x=int(input("Enter Water contained in gallons for 4-gallons jug X:"))
y=int(input("Enter Water contained in gallons for 3-gallons jug Y:"))
print("Current state:(X,Y)")
print("RULE:1 STATE:(4,Y|X<4)               PROCESS:Fill 4-gallon Jug")
print("RULE:2 STATE:(X,3|Y<3)               PROCESS:Fill 3-gal jug")
print("RULE:3 STATE:(X-d,Y|X>0)             PROCESS:Pour some water from 4-gal to 3-gal jug ")
print("RULE:4 STATE:(X,Y-d|Y>0)             PROCESS:Pour some water from 3-gal to 4-gal jug")
print("RULE:5 STATE:(0,Y|X>0)               PROCESS:Empty 4-gal jug")
print("RULE:6 STATE:(X,0|Y>0                PROCESS:Empty 3-gal jug")
print("RULE:7 STATE:(4,Y-(4-X)|X+Y>=3^X>0)  PROCESS:Pour water from 4-gal to 3-gal jug until its full")
print("RULE:8 STATE:(X-(3-Y),3|X+Y>=4^Y>0)  PROCESS:Pour water from 3-gal to 4-gal jug until its full")
print("RULE:9 STATE:(X+Y,0|X+Y<=4^Y>0)      PROCESS:Pour water from 3-gal to 4-gal jug")
print("RULE:10 STATE:(0,X+Y|X+Y<=3^X>0)     PROCESS:Pour water from 4-gal to 3-gal jug")
while True:
    ruleNo=int(input("Enter the Rule No:"))
    if ruleNo==1:
        if x<4:x=4
    if ruleNo==2:
        if y<3:y=3
    if ruleNo==5:
        if x>0:x=0
    if ruleNo==6:
        if y>0:y=0
    if ruleNo==7:
        if x+y>= 4 and y>0:x,y=4,y-(4-x)
    if ruleNo==8:
        if x+y>=3 and x>0:x,y=x-(3-y),3
    if ruleNo==9:
        if x+y<=4 and y>0:x,y=x+y,0
    if ruleNo==10:
        if x+y<=3 and x>0:x,y=0,x+y
    print("X =" ,x)
    print("Y =" ,y)
    if (x==2):
        print(" The result is a Goal state")
        break
