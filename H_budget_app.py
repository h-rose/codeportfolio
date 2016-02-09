
def add_item():
	item_dict = {} #if it's only used w/in the function, put here, not above (global)
	item_dict["name"] = raw_input("Name of item: ")
	item_dict["amount"] = raw_input("Amount: ")
	item_dict["monthly"] =raw_input("Monthly Payment: ")
	print item_dict
	return item_dict


def show_items(array):
	for index, item_dict in enumerate(array):	# to print all items w/ index & names
		print "User: " + str(index + 1) + " Name: " + item_dict["name"] + " Amount: " + item_dict["amount"] + " Monthly Payment: " + item_dict["monthly"]

def remove_item(array):
	show_items(array)
	needs_int = True
	while needs_int:
		needs_int = ask_for_number_and_delete(array)

def ask_for_number_and_delete(array):
	try:
		response_int = int(raw_input("Based on the index, which do you want to delete? Enter a number. \n"))
	except: 
		print "...Sorry, please enter a NUMBER... \n"
		return True
	else:
		del array[(response_int -1)]
		return False	#needs_int is now False

def save_items(array): #saves item in csv
	new_header = "name, amount, monthly \n"
	for dictionary in array:
		new_header += dictionary["name"] +", "+ dictionary["amount"] + ", " + dictionary["monthly"] + "\n"
	with open("budget", "w+") as f:
		f.write(new_header)

def read_items(array): #reads item in csv
	with open("budget", "r") as f:
		read_lines = f.readlines()
		start_reading = read_lines[1:]
		for string in start_reading: 
			split_line = string.split(",")
			name = split_line[0]
			amount = split_line[1]
			monthly = split_line[2].strip["\n"]
			item_dict = {"name": name, "amount": amount, "monthly": monthly}
			array.append(item_dict)
	return array


def ui_function():

	all_items_array = [] # will add dict to this. must return the function to add it.
	options = "please choose from options: \na) add item \ns) show item \nsave) save file \nread) read file \nr) remove item \nq) quite \n"
	user_choice = ""

	while user_choice != "q": #while not being asked to quit
		user_choice = raw_input(options)
		if user_choice =="a":
			item_dict_outer = add_item()
			all_items_array.append(item_dict_outer)
			print all_items_array
		elif user_choice == "s":
			show_items(all_items_array)
		elif user_choice == "save":
			save_items(all_items_array)
		elif user_choice == "read":
			read_items(all_items_array)	
		elif user_choice == "r":
			remove_item(all_items_array)
		elif user_choice == "q":
			break
        else:
			print "please enter a valid command"

ui_function()



