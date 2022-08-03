# # Duplicate Image Finder

# Description

It is used to detect the same images with several different methods and to observe the similarity rates of the images.

## Requirements

First, establish this python file to the location of the file you are in.
You may install requirements needed library on your local machine with the line below:

    $ pip install requirements.txt

## Basic Usage

You can import this library in your own working environment with the code below.

    from duplicate_image_finder import duplicate_image_finder


### Searched Method

Use the following function to make duplicate_image_finder search for duplicates within one specific folder and its subfolders:

    a = duplicate_image_finder(args)  
    a.searched()
  
### Move Method

After the searched method, you can move duplicate images to a selected directory with the code below:

    a = duplicate_image_finder(args)  
    a.move()

### Delete Method

After the searched method, you can delete duplicate images with the code below:

     a = duplicate_image_finder(args)  
     a.delete()

> ***Note:*** Moves the pictures to be deleted to an automatically created directory name $location$_del. Thus, it provides the opportunity to check the deleted images.

### Duplicate Csv Method

After the searched method, it creates the csv file of deleted images names with code below:

     a = duplicate_image_finder(args)  
     a.duplicate_csv()

> ***Note: The functions described above were built using the DifPy library.***


### Cosine Method

Similarity ratios between images can be found using cosine similarity. It also moves images that have a similarity ratio greater than the specified threshold value to a different directory. Code is given below:

     a = duplicate_image_finder(args)  
     a.cosine()
 
### Histogram Method

Similarity ratios between images can be found using histogram similarity. It also moves images that have a similarity ratio greater than the specified threshold value to a different directory. Code is given below:

     a = duplicate_image_finder(args)  
     a.histogram()

### Ssim Method

Similarity ratios between images can be found using structural similarity. It also moves images that have a similarity ratio greater than the specified threshold value to a different directory. Code is given below:

     a = duplicate_image_finder(args)  
     a.ssim()

## Comparison of the Methods

|                | Comparison                     | Recommended                      |
|----------------|-------------------------------|-----------------------------|
|Accuracy  |DifPy > Histogram > Ssim > Cosine         | DifPy         |
|Speed     |DifPy  > Cosine  > Histogram > Ssim       | DifPy         |
|Similarity Ratio | Histogram > Ssim > Cosine | Histogram |

In general, it is recommended to use the DifPy methods.

## CLI Usage

You can make use of duplicate_image_finder through the CLI interface by using the following commands:

    python duplicate_image_finder.py method1 $LOCATION $DESTINATION  
