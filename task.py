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
    else: 
        print("No argument passed. \nTry:", actions)

def taskadd(tasks, desc):
    todo = tasks["todo"]
    if todo: 
        id = len(todo) + 1
        dt = datetime.datetime.now(timezone.utc)
        dt = dt.strftime("%m/%d/%Y, %H:%M:%S")
        t = {"id": id, 
             "description": desc,
             "status": "todo",
             "createdAt": dt, 
             "updatedAt": dt
             }
        todo.append(t)
        with open(path_w, "w") as json_file: 
            json.dump(tasks, json_file)
        with open(path_w, "r") as json_file:
            to_do = json.load(json_file)
        print(to_do)
    else: 
        dt = datetime.datetime.now(timezone.utc)
        dt = dt.strftime("%m/%d/%Y, %H:%M:%S")
        t = {"id": 1, 
             "description": desc,
             "status": "todo",
             "createdAt": dt, 
             "updatedAt": dt
             }
        todo.append(t)
        print("task added:\n", todo)
        with open(path_w, "w") as json_file:
            json.dump(tasks, json_file)
    
def tasklist(tasks):
    if tasks: 
        print(tasks)
    else: 
        print('no current todo list, try adding a task')
if __name__ == "__main__":
    main()
    