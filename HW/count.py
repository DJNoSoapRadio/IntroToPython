# input the integers 
integers = input("Enter integers between 1 and 100, inclusive: ").split(' ')   
# converting to intgers
integers = [int(num) for num in integers]
# array for storing count of every numbers
count= [0]*100
# increasing count of numbers that are entered
for num in integers:
    count[num-1]+=1
# printing result
for num in range(100):
    if count[num]==1:
        print(str(num+1)+" occurs 1 time")
    elif count[num]>1:
        print(str(num+1)+" occurs "+str(count[num])+" times")