import xml.etree.ElementTree as ET
from xml.dom.minidom import parse, parseString
import sys, os

# have all xml files in the same folder and input folder/folder loc

if __name__ == "__main__":
    #get current dir, folder input should just be the folder name and in same loc as this file
    currdir = os.getcwd()
    allfiles = sys.argv[1]
    for file in os.listdir(currdir & "/" & allfiles):
        if file.endswith(".xml"):
            print(file)