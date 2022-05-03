from tkinter import *


pizza =Tk()
pizza.geometry("600x500") #Tkinter Box Size
pizza.title("Pizza on Demand") # Title

#<Name Entry>
name_label = Label(pizza, text="Name")
name_label.grid(row=0,column=0)#Location
#Name Text box size
name_entry = Entry(pizza,width=30)
name_entry.grid(row=0, column=1)#Location

#<Address>
address_label = Label(pizza, text="Address")
address_label.grid(row=1,column=0)

address_entry = Entry(pizza,width=30)#Address Text box size
address_entry.grid(row=1, column=1)#Location

#<Phone>
phone_label = Label(pizza, text="Phone Number")
phone_label.grid(row=2,column=0)

phone_entry = Entry(pizza,width=30)#Phone Text box size
phone_entry.grid(row=2, column=1) #Location



#<create Pizza List>

#Topping Options
my_pizza_list = ["Pepperoni","Mushrooms","Onions", "Sausage", "Black Olives","Green Peppers", "Pineapple","extra cheese", "Spinach","No Toppings"]

#List box function
pizza_List = Listbox(pizza, selectmode=MULTIPLE, bg="black", fg="red")
pizza_List.grid(row=4, column=1)#List Box Location

for item in my_pizza_list:
        pizza_List.insert(0,item)



add_button = Button(pizza, text="Add Pizza")
add_button.grid(row=5, column=0)

check_button = Button(pizza, text="chechout")
check_button.grid(row=6, column=0)

del_button = Button(pizza, text="Delete Order")
del_button.grid(row=7, column=0)

pizza.mainloop() #Loop