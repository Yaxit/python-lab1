activities = []
cmd = "5"
while not cmd == "4":
    print("1 - Insert\n2 - Remove\n3 - View\n4 - Quit\n")
    cmd = input("Cosa vuoi fare?\t")
    if cmd == "1":
        line = input("Insert title\t")
        activities.append(line)
    elif cmd == "2":
        num = input("Quale?\t")
        activities.remove(num)
    elif cmd == "3":
        for i in activities:
            print(i)
    elif cmd == "4":
        break
