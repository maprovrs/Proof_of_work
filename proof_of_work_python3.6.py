
import hashlib

string = "maprovrs"

complete = False
n = 0

while complete == False:
    curr_string = string + str(n)
    print (curr_string)

    curr_hash = hashlib.sha256(curr_string).hexdigest()
    n = n + 1

    print (curr_hash)
    if curr_hash.startswith('000'):
        print (curr_hash)
        print (curr_string)
complete = True

