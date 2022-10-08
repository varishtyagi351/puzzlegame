s1=["father","barke","cry","green","aeroplane"]
s2=("raehtf","kabre","Cyrotno","reneg","arelopnae")
score=0

for e in s2:
        print(e)
        a=input("Enter The Word you want to correct = \n")
        if a in s1:
         print("Your puzzle is correct")
         score=score+1
        else:
            print("Incorrect your puzzle")
            score=score-1
            
            
       
print("Your final score is ",score) 
print()               