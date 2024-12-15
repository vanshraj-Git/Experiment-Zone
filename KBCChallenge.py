import time
def greetings(p):
 if(p>0 and p<=12):
        print("Good morning,Sir")
 elif(p>12 and p<=17):
        print("Good afternoon,Sir")
 elif(p>17 and p<=20):
        print("Good evening,Sir")
 elif(p>20 and p<=24):
        print("Good morning,Sir")

c=int(time.strftime('%H'))
greetings(c)

a=(input("Enter Your name :-"))
z=["Question 1.:-","Question 2.:-","Question 3.:-"]
y=["Capital of India","Total states in India","Oldest language known to human kind"]
x=["Option A:- Gujarat","Option B:- Uttar Pradesh","Option C:- Delhi","Option D:- Rajasthan",]
w=["Option A:- 29","Option B:- 28","Option C:- 27","Option D:- 26",]
v=["Option A:- Roman","Option B:- Latin","Option C:- Hindi","Option D:- Sanskrit",]

a1=input("Are you ready!!!\nTo play the KBC!!!:- ")
if a1=='Yes' or a1=='yes':
    print(f"{a},here on your screen is your first question\n{z[0]} {y[0]}\n{x}")
    time.sleep(4)
    a2=input("Choose your answer wisely among the four one is your charm that will make you a millinaire:-")
    if a2=='c' or a2=='C' or a2=='option c' or a2=='Option c' or a2=='Option C' or a2=='option C'or a2=='optionc'or a2=='Optionc':
        time.sleep(3)
        print('You won your first million rupees!!!')
        time.sleep(2)
        a3=input("Now do you want to take the money and leave or Do you want to risk this million for another million.\nThe choice is yours, do you want to proceed to question 2 'Yes' or 'No':- ")
        if a3=='Yes' or a3=='yes':
            print(f"{a},here on your screen is the next question \n{z[1]} {y[1]}\n{w}")
            time.sleep(2)
            a4=input("Choose your answer wisely among the four one is your charm that will make you a millinaire:-")
            if a4=='a' or a4=='A' or a4=='option a' or a4=='Option a' or a4=='Option A' or a4=='option A'or a4=='optiona'or a4=='Optiona':
                time.sleep(4)
                print("You have won another million rupees!!!\n Now you've won 2 million!!!")
                time.sleep(2)
                a5=input("Now do you want to take the money and leave or Do you want to risk this million for another million.\nThe choice is yours, do you want to proceed to question 3 'Yes' or 'No':- ")
                if a5=='Yes' or a5=='yes':
                    time.sleep(2)
                    print(f"{a},here on your screen is the next question \n{z[2]} {y[2]}\n{v}")
                    time.sleep(1)
                    a6=input("Choose your answer wisely among the four one is your charm that will make you a millinaire:-")
                    if a6=='d' or a6=='D' or a6=='option d' or a6=='Option d' or a6=='Option D' or a6=='option D'or a6=='optiond'or a6=='Optiond':
                        time.sleep(5)
                        print('You have won another million!!!.\n',time.sleep(1),'The amount has been credited into your account.Enjoy!!!')
                    else:
                        time.sleep(5)
                        print("i am sorry to say this but unfortunately your answer is wrong\nYou have lost all your money")
                else:
                    print(f"We respect your decision {a}, you are exiting with 2 million rupeess")  
            else:
                time.sleep(5)
                print("i am sorry to say this but your answer is wrong\nYou have lost all your money")  
        else:
            print(f"We respect your decision {a}, you are exiting with 1 million rupees")   
    else:
        time.sleep(5)
        print("i regret to say this but your answer is wrong\nWe had a good time seeing you")
else:
    print("We are sorry to hear that you are exiting so soon")
                    
            
            

          

