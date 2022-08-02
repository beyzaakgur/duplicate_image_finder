import shutil
from difPy import dif
import pandas as pd
import sys
import os


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

    def move(self):
        search = self.searched()
        for file in search[1]:
            path = os.path.join(self.location, file)
            if not os.path.exists(self.destination):
                os.mkdir(self.destination)
            shutil.move(path, self.destination)

    def delete(self):
        search = self.searched()
        for file in search[1]:
            path = os.path.join(self.location, file)
            directory = self.location + "_del"
            parent_dir = os.getcwd()
            directory = os.path.join(parent_dir, directory)
            if not os.path.exists(directory):
                os.mkdir(directory)
            shutil.move(path, directory)
# move
# delete
# threshold
# cosine similarity
# l2 similarity


def main():
    args = sys.argv[1:]
    if sys.argv[1] == "method1":
        a = difpy_mod(args)
        #a.searched()
        a.move()
        #a.delete()
    else:
        print("There is no library such as,", sys.argv[1])


if __name__ == "__main__":
    main()
