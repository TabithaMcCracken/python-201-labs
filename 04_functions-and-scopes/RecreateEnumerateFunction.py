# Create my own enumerate function
top_thanksgiving_foods = [
    "pie", 
    "turkey", 
    "ham", 
    "stuffing", 
    "potatoes", 
    "bread", 
    "green beans", 
    "cornbread", 
    "deviled eggs",
    "cranberries"]
your_fav = input("What is your favorite Thanksgiving food?").lower()


# My enumerate function
def my_enumerate(a_list):
    result = [] # Creates an empty list to store the index and value as tuples
    counter = 0 # Sets the index counter to 0
    for item in a_list:
        result.append((counter, item)) # Adds an index number and the value
        counter +=1
    return result

my_list = (my_enumerate(top_thanksgiving_foods))
print("Here are the top 10 thanksgiving foods:")

for key, value in my_list:
    print((key + 1), ": ", value)

flag = False
for key, value in my_list:
    if your_fav in value:
        flag = True
        print(f"Your favorite food ranked #{(key+1)}")

if flag == False:
    print("Your food was not found in the top 10 Thanksgiving foods.")