import re
import sys


def load_file():
    with open('responses.db') as rf:
        file = rf.read()

    return {r.split('::')[0].strip(): r.split('::')[1].strip() for r in file.strip().split('||')}

message = ' '.join(sys.argv[1:])
responses = load_file()
for response in responses:
    if re.match(response[0], message):
        print(response[1])
        sys.exit()
