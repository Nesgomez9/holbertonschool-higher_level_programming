#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
        except:
            print("")
            return(i)
    i += 1 if i != 0 else i
    print("")
    return(i)
