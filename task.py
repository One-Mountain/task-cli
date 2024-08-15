import sys
import json

def main():
    #grab the command line arguments
    args = sys.argv[1:]
    #grab the path to the json file list
    path_w = 'task_list.json'
    #if it doesn't exist, create it
    try: 
        with open(path_w, mode = 'x') as json_file: 
            pass 
    except FileExistsError:
        pass
    # list of acceptable actions: 
    actions = ['add', 'update', 'delete', 'list', 'mark', 'help']
    # check for user input and compare to accepted actions
    if args: 
        print("Argument passed:", args)
        if args[0] not in actions:
            print("Invalid request:", args[0], "\nTry:", actions)
        else: 
            print("implementing action")
    else: 
        print("No argument passed. \nTry:", actions)
    #with open(path_w) as json_file: 
      #  l = json.load(json_file)
    
    #json_dump(data, json_file) to write to file
        
if __name__ == "__main__":
    main()
    