#string methods 〰️
#5   (00:25:13​) type cast 💱
#6   (00:30:14​) user input ⌨️
#7   (00:36:50​) math functions 🧮
#8   (00:40:58​) string slicing ✂️

#4

name="Bro"
print(len(name)) #to find the length of string
print(name.find("r")) #to find the index of the letter in string
print(name.capitalize())#only first letter of your string is capatalized
print(name.upper())# to capatilize whole string
print(name.lower())# to make whole string small letters
print(name.isdigit())#to check if it contain digits True or False
print(name.isalpha())#to check alphabetic letters but no spaces in b/w the string words
print(name.count("o"))#to count how many times a letter is present in the string
print(name.replace("o","a"))#to replace a letter with another letter
print(name*3)#to repeat the string multiple times
print(name*3)#to print the string multiple times

#5 typecast to convert the data type of a value to another data type
x, y, z= 1, 2.2, "3"
#print(type(x))
print(int(z*3)) # o/p is 9
print(z*3)# o/p is 333

#6 user input
name=input("enter your name")

#7 math functions
import math
pi=3.14
print(round(pi)) #to round up a num
print(math.ceil(pi)) #to round up a num to the highest value
print(abs(pi)) #to get absolute valuefrom zero
print(pow(pi,2)) #to get power of a num
print(math.sqrt(4)) # for asq root
print(max(1,4,6))# to get max value
#similarly min

# 8 string slicing= create a substring by extracting elements from another strings : indexing[], slice[]
#[start:stop:step]

name="Radhika Mittal"
f=name[2]
print(f) #2
f=name[-2]
print(f) #l
f=name[0:4] # or [:4] #stopping index is exclusive
print(f) #Radh
f=name[3:]
print(f) #hika Mittal
f=name[0:9:2]#1,3,5,7 index are included
print(f) #Rhi ia
f=name[::-1]# counting in reverse
print(f) #latttiM akihdaR

website= "https:// google.com"
slice=slice(7, 15,1)
print(website[slice]) #google.c
slice=slice(7,-4)# from backward wee count it as -1,-2,-3, ....
print(website[slice]) #google



