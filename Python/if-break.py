#9   (00:51:52​) if statements 🤔
#10 (00:58:19)​ logical operators 🔣
#11 (01:04:03​) while loops 🔄
#12 (01:07:31​) for loops ➰
#13 (01:13:04​) nested loops ➿
#14 (01:17:08) break continue pass ⛔

#9
if age==2:
    print("yes")
elif age==3:
    print("no")
else: 
    print("maybe")

#10 logical opt
and / or/not(condition)

#11 while
i=0
while(i<=2):
    print(i)
    i+=1
name=""
while len(name) ==0:
    name= input("enter")
#other way to wrrite it
name=None
while not name:
    name=input("enter")

#12 for loop
for i in range(10): #range(50,101)
    print(i) #0-9 50=100 add 101+1 to get 101 as well as 101 is exxlusive
for i in range(0,20+1,2):# start, stop, step
    print(i) #0,2,4,6,...it is just like indexing 
for i in "Radhika":
    print(i) 
#R
#a
#d
#h
#i
#k
#a

import time
for sec in range(10,0,-2):
    print(sec)
    time.sleep(2)
print("Yahoo!!!!")

#13 nested loop
row=3
col=3
sysmbol= input("enter it")
for i in range(row):
    for j in range(col):
        print(sysmbol, end="") # to print in same lin (end="" is used)
    print() #to print in new line

#14 break continue pass
#break= used to terminate the loop
#continue= used to skip an iteration of the loop
#pass= mostly used as a placeholder
num=123-456-67890
for i in range(num):
    if i=="-":
        continue
    print(i, end="")#12345667890

#if printing value from1-13
# if i==11: pass then 11 wont be printed