import hashlib

string = "MAPROVRS"

complete = False
n = 0

while complete == False:
    curr = string + str(n)
    curr_string = curr.encode()
    print (curr_string)

    curr_hash = hashlib.sha256(curr_string).hexdigest()
    n = n + 1
    print(curr_hash)

    if curr_hash.startswith('000000'):

        print("\033[1;31;40m Resultat \n")
        print("hash = ", curr_hash)
        print("new string ", curr_string)
        print("n = ", n)
        complete = True
