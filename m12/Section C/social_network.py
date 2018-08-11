# *************** file io ********************************************
def parse_line(line):
	line = line.replace(".\n","")
	line = line.split(" is followed by ")
	network_dict[line[0]] = line[1].split(",")

def load_data():
	print("Loading the file...")
	in_file = open("user_names_and_friends_list.txt","r")
	line = in_file.readline()
	while line:
		parse_line(line)
		line = in_file.readline()

# *************** console i/o*****************************************
def load_data():
	line = input()
	line = line.split(".\n")
	for i in line:
		i = i.split(" is followed by ")
		network_dict[i[0]] = i[1].split(",")

# *************** n/w functions **************************************
def print_network():
	for user_profile in network_dict:
		print(user_profile+": "+", ".join(network_dict[user_profile]))

def validate(user_name):
	if user_name in network_dict:
		return True
	return False

def add_follower(user_1, user_2): # user 2 is following user 1
	if not validate(user_1) or not validate(user_2):
		return "Either of the users are not in the network!!"
	network_dict[user_1].append(user_2)
	print("Connection added successfully!!")

def get_followers(user): # all followers of user
	if not validate(user):
		return "Invalid profile name"
	return network_dict[user]

def is_following(user_1, user_2): # is user 1 following user 2
	if not validate(user_1) or not validate(user_2):
		return "Either of the users are not in the network!!"
	if user_1 in network_dict[user_2]:
		return True
	return False

def remove_follower(user_1, user_2): # remove user 2 from user 1's followers list
	if not validate(user_1) or not validate(user_2):
		return "Either of the users are not in the network!!"
	if user_2 in network_dict[user_1]:
		network_dict[user_1].remove(user_2)
		return "Connection removed"
	return user_2+" not found in "+user_1+" friends list"

def add_new_user(user_name):
	if validate(user_name):
		return user_name+" is already available!"
	network_dict[user_name] = []
	return "New user added!!"

def max_followers():
	max_frnds_count = 0
	social_user = []
	for user_name in network_dict:
		no_of_connections = len(network_dict[user_name])
		if no_of_connections > max_frnds_count:
			# social_user = user_name
			max_frnds_count = no_of_connections
	for user_name in network_dict:
		if len(network_dict[user_name]) == max_frnds_count:
			social_user.append(user_name)
	return ", ".join(social_user)

def main():
	load_data()
	print_network()
	# print(add_new_user("Prudhvik"))
	# print(add_follower("Prudhvik", "Debra"))
	# print(is_following("Prudhvik","Debra"))
	# print(is_following("Prudhvik","Jhon"))
	# print(is_following("Prudhvik","Siva"))
	# print(get_followers("Debra"))
	# print_network()
	# print(remove_follower("Prudhvik","Debra"))
	# print(get_followers("Prudhvik"))
	# print("most popular: "+max_followers())

if __name__ == "__main__":
	network_dict = {}
	main()
