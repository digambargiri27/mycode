import os 
import json

def main():
    os.chdir("/home/student")
    with open("spacex.json", "r") as of:
        space_data = json.load(of)
        # test to ensure I can now work with the data in Python
        print(space_data)            # we should now see the data from the file
        print(type(space_data))      # the data type should be 'dict' NOT 'str'
        print(space_data.get('id'))  # perform a test lookup on a 'dict' data type
if __name__ == "__main__":
    main()

