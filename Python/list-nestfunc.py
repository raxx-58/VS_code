#15 (01:21:06​) lists 🧾
#16 (01:26:58​) 2D lists 📜
#17 (01:30:47​) tuples 📄
#18 (01:33:47​) sets 🍴
#19 (01:40:03​) dictionaries 📖
#20 (01:47:20​) indexing 📑
#21 (01:53:23​) functions 📞
#22 (02:02:03​) return statement 🔙
#23 (02:04:51) keyword arguments 🔑
#24 (02:07:09​) nested function calls 🖇️

            #15 lists - list is already a variable
list="to store multiple items in a single variable"
food=["pizza","burger","samosa","pasta"]
print(food) #['pizza', 'burger', 'samosa', 'pasta']
print(food[2]) #samosa
food[1]= milk
print(food) #['pizza', 'milk', 'samosa', 'pasta']
food.append("ice-cream") #to add item at the end
print(food) #['pizza', 'milk', 'samosa', 'pasta', 'ice-cream']
food.remove("samosa") #to remove an item specific
print(food) #['pizza', 'milk', 'pasta', 'ice-cream']
food.pop() #to remove last item

for x in food:
    print(x) #to print all items one by one
#pizza
#milk
#pasta
#ice-cream
food.sort() #to sort the items in alphabetical order
print(food) #['ice-cream', 'milk', 'pasta', 'pizza']
food.clear() #to clear the whole list
print(food) #[]

            #16 2D lists
drinks=["coke","pepsi","fanta"]
dinner=["pizza","burger","samosa"]
dessert=["ice-cream","cake"]
food=[drinks,dinner,dessert]
print(food) #[['coke', 'pepsi', 'fanta'], ['pizza', 'burger', 'samosa'], ['ice-cream', 'cake']]
print(food[0]) #['coke', 'pepsi', 'fanta']
print(food[0][1]) #pepsi

            #17 tuples - it is immutable (cannot be changed)
#tuples are faster than lists they are ordered and are used to group together realted data
student=("Raxx", 19, "Female")

print(student.count("Raxx")) #1
print(student.index(19)) #1

for x in student:
    print(x)
#Raxx
#19
#Female

if "Raxx" in student:
    print("yes") #yes

            #18 sets - it is unordered and unindexed (no duplicates allowed)

utensils = {"fork","spoon","knife"} 
for x in utensils:
    print(x)
#knife
#fork
#spoon
utensils = {"fork","spoon", "spoon","spoon","knife"} 
for x in utensils:
    print(x)
#knife
#fork
#spoon
#always gives random value
utensils.add("napkin") #to add an item
print(utensils) #{'fork', 'spoon', 'knife', 'nap
utensils.remove("fork") #to remove an item
print(utensils) #{'spoon', 'knife', 'napkin'}
utensils.clear() #to clear the whole set
print(utensils) #set()

dishes={"biryani","pasta","pizza"}
utensils.update(dishes) #to add 2 sets
for x in utensils:
    print(x)
#pasta
#biryani
#spoon
#knife
#napkin
print(len(utensils)) #5

dinner_table= utensils.union(dishes) #to join 2 sets
print(dinner_table) #{'pasta', 'biryani', 'spoon',

print(utensils.difference(dishes)) #to find what utensils has that dishes doesnot
#{'spoon', 'knife', 'napkin'}

            #19 dictionaries - it is unordered, changeable collection of unique key:value pairs
#Fast beacuse they use hashing, allow us to access a value quickly
country= {'India':'ND', 'USA':'DC', 'china': 'beging'}
#india is key ND is value
print(country['USA']) #DC
 


