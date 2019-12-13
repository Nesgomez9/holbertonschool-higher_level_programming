#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    argc = len(argv) - 1
    print("{} argument{}{}".format
          (argc, "" if argc == 1 else "s", ":" if argc else "."))

    if argc:
        for i, av in enumerate(argv):
            if i:
                print("{}: {}".format(i, av))
