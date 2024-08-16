import sys
import json
import datetime
from datetime import timezone 

path_w = 'task_list.json'
def main():
    #grab the command line arguments
    args = sys.argv[1:]
    #grab the path to the json file list
    #if it doesn't exist, create it
    try: 
        with open(path_w) as json_file: 
            l = json.load(json_file) 
    except:
        l = {"todo":[]}
            
    # list of acceptable actions: 
    actions = ['add', 'update', 'delete', 'list', 'mark', 'help']
    # check for user input and compare to accepted actions
    if args: 
        if args[0] not in actions:
            print("Invalid request:", args[0], "\nTry:", actions)
        else: 
            print("implementing action")
            #action was addition: 
            if args[0] == "add":
                if not len(args) == 2: 
                    print("Please add task description in quotes")
                else: 
                    taskadd(l, args[1])
            elif args[0] == "list":
                if len(args) == 1: 
                    #only the word list
                    tasklist(l["todo"])
                elif len(args) == 2:
                    if args[1] == "done":
                         tasklist(l["todo"], "done")
                    elif args[1] == "todo":
                         tasklist(l["todo"], "todo")
                    elif args[1] == "in-progress":
                         tasklist(l["todo"], "in-progress")
                    else: 
                        print("Invalid request: ", args)
                else: 
                    print("Invalid request:", args)
            elif args[0] == "mark": 
                 if len(args) != 3:
                     print("Invalid request: ", args)
                 else:
                     if args[1] != "done" and args[1] != "in-progress":
                        print("Invalid request: ", args)
                        print("Task can be marked in-progress or done")
                     else: 
                         if args[2].isdigit(): 
                             taskmark(l, args[1], int(args[2])) 
                         else: 
                             print("Invalid request: ", args)
                             print("Provide an id number for task")
    else: 
        print("No argument passed. \nTry:", actions)
def id_counter(tasks):
    li = tasks['todo']
    if li: 
        last_task = len(li)-1
        return li[last_task]["id"] + 1
    else: 
        return 1
    
def taskadd(tasks, desc):
    todo = tasks["todo"]
    if todo: 
        dt = datetime.datetime.now(timezone.utc)
        dt = dt.strftime("%m/%d/%Y, %H:%M:%S")
        t = {"id": id_counter(tasks), 
             "description": desc,
             "status": "todo",
             "createdAt": dt, 
             "updatedAt": dt
             }
        
        
        todo.append(t)
        with open(path_w, "w") as json_file: 
            json.dump(tasks, json_file)
    else: 
        dt = datetime.datetime.now(timezone.utc)
        dt = dt.strftime("%m/%d/%Y, %H:%M:%S")
        
        t = {"id": id_counter(tasks), 
             "description": desc,
             "status": "todo",
             "createdAt": dt, 
             "updatedAt": dt
             }
        
        todo.append(t)
        with open(path_w, "w") as json_file:
            json.dump(tasks, json_file)
    
def tasklist(tasks, status= "all"):
    if tasks:
        if status == "all": 
            for task in tasks:
                print(task)
        else:
            count = 0 
            for task in tasks:
                if task["status"] == status:
                    print(task)
                    count = count + 1
            if count == 0:
                print("No tasks marked with status " + status)
    else: 
        print('no current todo list, try adding a task')

def taskmark(tasks, mark, id):
    todo = tasks["todo"]
    updated_list = {"todo":[]}
    valid_id = False
    valid = False
    for t in todo:
        if t["id"] == id: 
            valid_id = True
            if t["status"] == mark:
                print('task mark is already', mark)
            else:
                valid = True
                t["status"] = mark
                dt = datetime.datetime.now(timezone.utc)
                dt = dt.strftime("%m/%d/%Y, %H:%M:%S")
                t["updatedAt"] = dt
        updated_list["todo"].append(t)
    if not valid_id:
        print("Invalid id. Try again")
    elif not valid: 
        pass
    else: 
        with open(path_w, "w") as json_file:
            json.dump(updated_list, json_file)
if __name__ == "__main__":
    main()
    