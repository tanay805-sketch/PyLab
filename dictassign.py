def add_entry(my_dict, key, value):
    my_dict[key] = value

def reassign_dict(new_data):
    global user_dict
    user_dict = new_data

user_dict = {"name": "Akil"}
print("Original:", user_dict)

add_entry(user_dict, "age", 30)
print("After add_entry:", user_dict)

reassign_dict({"item": "phone", "price": 10000})
print("After reassign_dict:", user_dict)



