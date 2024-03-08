print("welcome to my quiz !!");

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()


score = 0

print("okay! Let's play :)")
    
answer = input("what does HTML stand for? ").lower()

print(answer)

if answer == "hyper text markup language":
    print("Correct!") 
    score += 1
else:
    print("Incorrct!")    
       
answer = input("Who was the father of science? ").lower()

if answer == "albert einstein":
    print("Correct!") 
    score += 1
else:
    print("Incorrct!")   
    
    
answer = input("what is the fullform of QR? ").lower()

if answer == "quick response":
    print("Correct!") 
    score += 1
else:
    print("Incorrct!")   

answer = input("what does CPU stand for? ").lower()

if answer == "central processing unit":
    print("Correct!") 
    score += 1
else:
    print("Incorrct!")   

answer = input("Who was current prime minister of Nepal? ").lower()


if answer == "Prachande":
    print("Correct!") 
    score += 1
else:
    print("Incorrct!")    
    
print("you have got " + str(score) + " corrct answer " )  


percentage = (score/4) * 100

print("You have got " + str(percentage) + "%. " )              
    
    