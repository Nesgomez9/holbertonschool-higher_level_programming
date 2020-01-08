#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        print("")
        i += 1
        return (i)
    except:
        print("")
        return(i)
