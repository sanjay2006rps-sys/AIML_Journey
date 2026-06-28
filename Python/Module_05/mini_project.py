skills = set()

while True:
    choice = input("1.Add  2.Remove  3.Show  4.Exit: ")
    if   choice == "1": skills.add(input("Skill: "))
    elif choice == "2": skills.discard(input("Remove: "))
    elif choice == "3": print(skills)
    elif choice == "4": break