import re
import sys
import os

if not os.path.exists('responses.db'):
    open('responses.db').close()

def load_file():
    with open('responses.db') as rf:
        file = rf.read().strip()
        if file[-2:] == ';;':
            file = file[:-2]

    return {r.split('::')[0].strip(): r.split('::')[1].strip() for r in file.strip().split(';;')}

message = ' '.join(sys.argv[1:])
responses = load_file()
for response in responses:
    if re.search(response, message):
        print(responses[response])
        sys.exit()
