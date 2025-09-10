li=input("initial_menu")
initial_menu=li.split()
print(initial_menu)
add_item=input("add_item")
initial_menu.append(add_item)
remove_item=input("remove_item")
initial_menu.remove(remove_item)
check_item=input("check_item")
print("Updated Menu :",initial_menu)
if(check_item in initial_menu):
    print(f"Availabilty : {check_item} is available")
else:
    print(f"Availability : {check_item} is not available")