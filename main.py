
import shutil
import os
from difPy import dif
import pandas as pd

location="disgust" # location of pictures
search = dif(location)

search.result

search.lower_quality

df = pd.DataFrame(search.lower_quality)
df.to_csv("disgust.csv")

files=[]

for i  in search.lower_quality:
  files.append(i[len(location)+1:])

print(files)
len(files)

search.stats

destination = "move/disgust"

for file in files:
    path = os.path.join(location, file)
    shutil.move(path, destination)

# importing os module
import os
# Path
for file in files:
  path = os.path.join(location, file)
  # Remove the file
  # 'file.txt'
  os.remove(path)

