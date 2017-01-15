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

    responses = []
    for r in file.strip().split(';;'):
        responses.append(map(lambda x: x.strip(),r.split('::')))

    return responses

message = ' '.join(sys.argv[1:])#.replace('\n',' ')
responses = load_file()
for response in responses:
    x = re.search(response[0], message)
    if x:
        print(re.sub(response[0], response[1], x.group(0)))
        #sys.exit()
