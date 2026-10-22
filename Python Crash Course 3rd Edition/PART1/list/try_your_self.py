Guest_List=['swapnil','shubham','gulshan']

print(f"{Guest_List[0].title()} You are welcome for dinner")
print(f"{Guest_List[1].title()} You are welcome for dinner")
print(f"{Guest_List[2].title()} You are welcome for dinner")
# 3-4. Guest List:

print(f"{Guest_List[1].title()} ok you rejected the invatation ")

#  3-5. Changing Guest List:

Guest_List[1]='rishi'

print(f"{Guest_List[1].title()} Yor are welcome for dinner ")

# 3-6. More Guests:

Guest_List.insert(0,"rasushan")
Guest_List.insert(2,"salman")
Guest_List.append("rohit")

print(f"{Guest_List[0].title()} You are welcome for dinner")
print(f"{Guest_List[1].title()} You are welcome for dinner")
print(f"{Guest_List[2].title()} You are welcome for dinner")
print(f"{Guest_List[3].title()} You are welcome for dinner")
print(f"{Guest_List[4].title()} You are welcome for dinner")
print(f"{Guest_List[5].title()} You are welcome for dinner")

# 3-7. Shrinking Guest List:

removed_guest = Guest_List.pop()
print(f"Sorry {removed_guest.title()}, I can't invite you.")

removed_guest = Guest_List.pop()
print(f"Sorry {removed_guest.title()}, I can't invite you.")

removed_guest = Guest_List.pop()
print(f"Sorry {removed_guest.title()}, I can't invite you.")

removed_guest = Guest_List.pop()
print(f"Sorry {removed_guest.title()}, I can't invite you.")

print(f"{Guest_List[0].title()} You are welcome for dinner")
print(f"{Guest_List[1].title()} You are welcome for dinner")

del Guest_List[0]
del Guest_List[0]

print(f"No Guest")




