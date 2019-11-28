# Moca News Image Downloader

## Introduction
Moca News Image Downloader is a simple command line program to download enlarged images from the [Moca News website](https://moca-news.net/). These images are right-clicked disabled on the website and accessing the direct link to the image will show an "X" image instead (see below). This program is used to download the intended images from the website. This program is written in Python 3.
![ban.jpg](/images/ban.jpg)

## Setting Up
1. Download and install the latest version of [Python](https://www.python.org/downloads/).
2. Open the Command Prompt (for Windows) or Terminal (for MacOS).
3. Run the following commands:
```
pip install requests
```

## Running the Program
1. Using the Command Prompt, change to the directory to where the file `moca_news_image_downloader.py` is located. E.g. `cd D:\moca_news_image_downloader`
2. Run the following command: `python moca_news_image_downloader.py <ID>`
   1. ID - Article ID (e.g. the article ID for the page "https://moca-news.net/article/20191016/2019101622300a_/01/" is "20191016/2019101622300a_")
   2. Examples:
      1. `python moca_news_image_downloader.py 20191016/2019101622300a_`
3. The image will be saved in the folder `moca-news/<Article ID>`. Based on the above example, the images are saved in the folder `moca-news/2019101622300a_`.
![image001.png](/images/img001.png)

## Additional Notes
1. If some of the images downloaded are the images with "X" (see below), delete these images and re-run the program with the same command to download the images again.
![ban.jpg](/images/ban.jpg)
