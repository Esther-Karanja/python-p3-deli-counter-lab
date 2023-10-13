#queue at the Deli at the start of the day
#use enumerate function to return index and what is in the index
katz_deli = []

#shows everyone their current place in the line
def line(katz_deli):
    if katz_deli == []:
        print("The line is currently empty.")
    else:
        display_message ="The line is currently:"
        #add 1 to start enumeration at 1 not 0
        for index,value in enumerate(katz_deli, 1):
            display_message += f" {index}. {value}"
        print(display_message)

line(["Esther", "Jane", "Sam"])


#add a new customer will use when entering the deli queue
def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position =len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")

take_a_number(["Esther", "Jane", "Sam"], "Ivy")

# call the next person in line and then remove them from the front
def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        being_served = katz_deli.pop(0)
        print(f"Currently serving {being_served}.")
        # print(katz_deli)

now_serving(["Esther", "Jane", "Sam", "Ivy"])

