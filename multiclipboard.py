# Jbpd
# Tutorial:
# Go into the command prompt, then cd to the folder that this program is located.
# Then, type 'pip install keyboard'
# Then, to enter commands, make sure you are on the dir where the file is located then type 'python multiclipboard.py <command>'
# The commands are:
#   save (saves the current content that you have on your clipboard to a key that you name)
#   load (type in the key in which you want the data from that key to be copied to your clipboard)
#   list (shows all of the keys that you made)
#   delete (deletes the content of the key entered)
#   erase (completely deletes the file that has the saved clipboard content)
# Hopefully this is useful!
import sys
import clipboard
import json
import os

SAVED_DATA = "clipboard.json"


def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}


def delete_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


def erase_all():
    try:
        os.remove("clipboard.json")
        clipboard.copy("")
        print("Clipboard successfully erased.")
    except:
        print("Cannot erase a file that does not exist!")


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    if command == "save":
        key = input("Enter a key name to create a new key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved")
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard.")
        else:
            print("Key does not exist.")
    elif command == "list":
        print(data)
    elif command == "delete":
        key = input("Enter a key: ")
        data[key] = ""
        delete_data(SAVED_DATA, data)
        print(f"Contents of {key} successfully deleted!")
    elif command == "erase":
        choice = input("Are you sure you want to delete everything? ")
        if choice == "yes":
            erase_all()
        else:
            print("Okay")
    else:
        print("Unknown command")
else:
    print("Please pass exactly one command.")
