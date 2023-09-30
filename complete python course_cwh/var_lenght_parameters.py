def avg(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("avg is:",sum/len(numbers))
avg(3,4,2,9,43)