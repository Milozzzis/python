import random
secret = random.randint(1,100 )
x = 0                
while True:           
    guess = int(input("Ваша догадка: "))
    x = x + 1        
    if guess < secret:
        print("больше") 
    elif guess > secret:
        print("меньше")  
    else:
        print("угадал, попыток:", x) 
        break
  
