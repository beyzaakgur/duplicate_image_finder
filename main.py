import shutil
from difPy import dif
import pandas as pd
import sys
import os
import imagehash
from PIL import Image


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
            shutil.move(path, self.destination)

    def delete(self):
        search = self.searched()
        for file in files:
            path = os.path.join(location, file)
            # Remove the file
            # 'file.txt'
            os.remove(path)


    ## Convert the picture to RGB
    # def make_regalur_image(self, img, size=(64, 64)):
    #    gray_image = img.resize(size).convert('RGB')
    #    return gray_image


#
## Calculate histogram
# def hist_similar(self, lh, rh):
#    assert len(lh) == len(rh)
#    hist = sum(1 - (0 if l == r else float(abs(l - r)) / max(l, r)) for l, r in zip(lh, rh)) / len(lh)
#    return hist
#
## Calculate similarity
# def calc_similar(self, li, ri):
#    calc_sim = self.hist_similar(li.histogram(), ri.histogram())
#    return calc_sim


# move
# delete
# threshold
# cosine similarity
# l2 similarity

def main():
    args = sys.argv[1:]
    if sys.argv[1] == "difPy":
        a = difpy_mod(args)
        #a.searched()
        a.move()
    else:
        print("There is no library such as,", sys.argv[1])

    # image1 = Image.open('ilPBHd3r3a.jpg')
    # image1 = a.make_regalur_image(image1)
    # image2 = Image.open('Johnny-Depp.jpg')
    # image2 = a.make_regalur_image(image2)
    # print("The similarity between pictures is", a.calc_similar(image1, image2))


if __name__ == "__main__":
    main()
