todo_list = []
while True:
    print("/n TO-DO list menu") 
    print("1.add task")
    print("2.remove task")
    print("3.view task")
    print("4.exit")
    choice = input("enter the choice : ")
    if choice == "1":
        task = input("enter the task : ")
        todo_list.append(task)
        print("task added")
    elif choice == "2":
        task = input("enter the task to remove")
        if task in todo_list:
            todo_list.remove(task)
            print("task removed")
        else:
            print("task not found")        
    elif choice == "3" :
        print ("task list") 
        for i in range(len(todo_list)):
                print(f"{i+1}.{todo_list[i]}")
    elif choice == "4":
        print("exit")
        break
    else:
        print("invalid choice")    
        