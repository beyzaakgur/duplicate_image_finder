import shutil
from difPy import dif
import pandas as pd
import sys
import os
import glob
from PIL import Image
import numpy as np
from scipy import spatial


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

    def cosine(self):
        paths = glob.glob(self.location + "/*")  # photos path

        final_weights = {}

        for i in range(len(paths)):
            weights = []
            img1 = Image.open(paths[i])
            img1_reshape = img1.resize((round(img1.size[0] * 0.5), round(img1.size[1] * 0.5)))
            img_array1 = np.array(img1_reshape)
            img_array1 = img_array1.flatten()
            img_array1 = img_array1 / 255
            for j in range(i + 1, len(paths)):
                img2 = Image.open(paths[j])
                img2_reshape = img2.resize((round(img1.size[0] * 0.5), round(img1.size[1] * 0.5)))
                img_array2 = np.array(img2_reshape)
                img_array2 = img_array2.flatten()
                img_array2 = img_array2 / 255

                similarity = -1 * (spatial.distance.cosine(img_array1, img_array2) - 1)
                if similarity >= 0.94:
                    weights.append([similarity, paths[j]])
            print(f"\rNumber of process: [{i}/{len(paths)}]", "[{}%]".format(int((i / len(paths)) * 100)), end="")
            if weights != []:
                final_weights[paths[i]] = weights

        files = []
        for i in list(final_weights.values()):
            for j in i:
                files.append(j[1])

        files = set(files)
        for file in files:
            path = file
            if not os.path.exists(self.destination):
                os.mkdir(self.destination)
            shutil.move(path, self.destination)

    def histogram(self):
        def make_regalur_image(img, size=(64, 64)):
            gray_image = img.resize(size).convert('RGB')
            return gray_image

        # Calculate histogram
        def hist_similar(lh, rh):
            assert len(lh) == len(rh)
            hist = sum(1 - (0 if l == r else float(abs(l - r)) / max(l, r)) for l, r in zip(lh, rh)) / len(lh)
            return hist

        # Calculate similarity
        def calc_similar(li, ri):
            calc_sim = hist_similar(li.histogram(), ri.histogram())
            return calc_sim

        paths = glob.glob(self.location + "/*")  # photos path
        final_weights = {}
        for i in range(len(paths)):
            weights = []
            image1 = Image.open(paths[i])
            image1 = make_regalur_image(image1)
            for j in range(i + 1, len(paths)):
                image2 = Image.open(paths[j])
                image2 = make_regalur_image(image2)
                # print("The similarity between pictures is", calc_similar(image1, image2))
                similarity = calc_similar(image1, image2)
                # print(similarity)
                if similarity >= 0.4:
                    weights.append([similarity, paths[j]])
            print(f"\rNumber of process: [{i}/{len(paths)}]", "[{}%]".format(int((i / len(paths)) * 100)), end="")
            if weights != []:
                final_weights[paths[i]] = weights

        files = []

        for i in final_weights.values():
            for j in i:
                files.append(j[1])

        files = set(files)

        for file in files:
            path = file
            if not os.path.exists(self.destination):
                os.mkdir(self.destination)
            shutil.move(path, self.destination)


# readme dosyası yazılsın
# pull request için farklı branch aç

def main():
    args = sys.argv[1:]
    if sys.argv[1] == "method1":
        a = difpy_mod(args)
        # a.searched()
        # a.move()
        # a.delete()
        # a.cosine()
        a.histogram()
    else:
        print("There is no library such as,", sys.argv[1])


if __name__ == "__main__":
    main()
