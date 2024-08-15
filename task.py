import sys
import json

def main():
    #grab the command line arguments
    args = sys.argv[1:]
    #grab the path to the json file list
    path_w = 'task_list.json'
    #if it doesn't exist, create it
    try: 
        with open(path_w) as json_file: 
            l = json.load(json_file) 
    except:
        l = {}
            
    # list of acceptable actions: 
    actions = ['add', 'update', 'delete', 'list', 'mark', 'help']
    # check for user input and compare to accepted actions
    if args: 
        #action was addition: 
        if args[0] == "add":
            if not len(args) == 2: 
                print("Please add task description in quotes")
            else: 
                taskadd(l, args[1])
        if args[0] not in actions:
            print("Invalid request:", args[0], "\nTry:", actions)
        else: 
            print("implementing action")
    else: 
        print("No argument passed. \nTry:", actions)
    #with open(path_w) as json_file: 
      #  l = json.load(json_file)
    
    #json_dump(data, json_file) to write to file
def taskadd(tasks, desc):
    if tasks: 
        print("tasks to do", tasks, desc)
    else: 
        print("task added", desc)
    
def tasklist(tasks):
    if tasks: 
        print(tasks)
    else: 
        print('no current todo list, try adding a task')
if __name__ == "__main__":
    main()
    