import itertools

def remove_junk(ptr,separators):
    newPtr = []
    for x in ptr:
        if not (x[0] in separators or x[-1] in separators):
            newPtr.append(x)
    return newPtr

def write_to_file(ptr, mx):
    with open("emails.txt",'a') as f:
        for x in ptr:
            f.write(''.join([str(elem) for elem in x]))
            f.write('@{0}\n'.format(mx))

def main():
    string = input("[+] Enter user info : ")
    string = string.split(";")
    mx=input("[+] Email provider : ")

    separators = ['','.','_','-']  #The most common separators people tend to use

    for s in separators:
        string += s
        ptr = itertools.permutations(string)
        newptr = remove_junk(ptr,separators[1:]) #Removes not so common email formats
        write_to_file(newptr,mx)
    print("[+] Emails generated and saved in emails.txt")

if __name__ == "__main__":
    main()
