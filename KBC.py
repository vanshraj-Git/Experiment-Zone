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
y=["Total number of subjects in your semister 1","When was covid-19 first appeared","Name of your HOD"]
x=["Option A:- 4","Option B:- 5","Option C:- 6","Option D:- 7",]
w=["Option A:- 2019","Option B:- 2020","Option C:- 2021","Option D:- 2022",]
v=["Option A:- mayank","Option B:- Darshan","Option C:- Don't know","Option D:- none of the above",]

def Question1():
    print(z[0],y[0])
    print(x)
    u=input("Too aap kya chunanga a,b,c ya d:- ")
    if(u=='d' or u=='D'):
        print("aap jit chuta hai 50 hazar ruppee")
    else:
        print("afsos aapka javab galat hai.")
def Question2():
    print(z[1],y[1])
    print(w)
    u=input("Too aap kya chunanga a,b,c ya d:- ")
    if(u=='a' or u=='A'):
        print("aap jit chuta hai 50 hazar ruppee")
    else:
        print("afsos aapka javab galat hai.")
def Question3():
    print(z[2],y[2])
    print(v)
    u=input("Too aap kya chunanga a,b,c ya d:- ")
    if(u=='a' or u=='A'):
        print("aap jit chuta hai 50 hazar ruppee")
    else:
        print("afsos aapka javab galat hai.")

Question1()
Question2()
Question3()