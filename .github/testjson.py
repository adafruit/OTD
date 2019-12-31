import sys
import os
import json

expectedkeys = ["Day of the year", "Person",
                "Notable for", "Year",
                "Accomplishment", "Web Reference"]
try:
    directory = sys.argv[1]
except IndexError:
    print("Must provide directory name as argument")
    exit(-1)

exitval = 0

for filename in os.listdir(directory):
    if not filename.endswith(".json"): 
        continue
    pathname = os.path.join(directory, filename)
    print(pathname)
    try:
        with open(pathname) as json_file:
            data = json.load(json_file)
            for k in expectedkeys:
                if not data.get(k):
                    print("No '"+k+"' key")
                    exitval = -1
    except json.decoder.JSONDecodeError as e:
        print("Could not decode valid JSON")
        print(e)
        exitval = -1
    print()

exit(exitval)
