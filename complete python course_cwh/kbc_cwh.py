questions=[
    ["which language was used to create fb?","pyhton","php","java","c","None"],
    ["which language was used to create fb?","pyhton","php","java","c","None"],
    ["which language was used to create fb?","pyhton","php","java","c","None"],
    ["which language was used to create fb?","pyhton","php","java","c","None"],
    ["which language was used to create fb?","pyhton","php","java","c","None"],
    ["which language was used to create fb?","pyhton","php","java","c","None"]
]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,1000000,5000000]
money=0
for i in range(0,len(questions)):
    ques=questions[i]
    print(f"\nquestion for rs.{levels[i]}")
    print(f"a.{ques[1]}   b.{ques[2]}")
    print(f"c.{ques[3]}   d.{ques[4]}")
    reply=int(input("enter your answer(1-4) or 0 to quit:\n"))
    if(reply==0):
        money=levels[i-1]
        break
    if(reply==ques[-1]):
        print(f"correct answer, you have won Rs.{levels[i]}")
        if(i==4):
            money=1000
        elif(i==9):
            money=320000
        elif(i==14):
            money=10000000
        else:
            print("wrong answer!")
            break
print(f"your take home money is {money}")
