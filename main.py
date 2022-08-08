from duplicate_image_finder import duplicate_image_finder as dif
import sys


def main():
    location = "surprise"
    destination = "surprise_rem"
    threshold = 0.94

    a = dif(location, destination)
    # a.searched()
    # a.move()
    # a.delete()
    # a.cosine()
    # a.histogram()
    # a.duplicate_csv()
    a.remove(a.cosine, threshold)

if __name__ == "__main__":
    main()
