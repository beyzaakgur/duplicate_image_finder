from PIL import Image
import imagehash

hash = imagehash.average_hash(Image.open('sad/sadchild_Large_1.jpg'))
print(hash)

otherhash = imagehash.average_hash(Image.open('sad/sadchild_Large_3.jpg'))
print(otherhash)

print(hash == otherhash)

print(hash - otherhash)

