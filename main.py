import shutil
from difPy import dif
import pandas as pd
import sys
import os
import imagehash


class difpy_mod(object):

    def __init__(self, *args):
        self.location = args[0][1]
        self.destination = args[0][2]
        # self.filepath = args[4]

    def searched(self):
        search = dif(self.location)
        files = []
        for i in search.lower_quality:
            files.append(i[len(self.location) + 1:])
        return [search, files]


# move
# delete
# threshold
# cosine similarity
# l2 similarity

def main():
    args = sys.argv[1:]
    if sys.argv[1] == "method1":
        a = difpy_mod(args)
        a.searched()
    else:
        print("There is no library such as,", sys.argv[1])


if __name__ == "__main__":
    main()
