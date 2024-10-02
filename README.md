# Leaf Component Identifier Tool

## Installation
### 1. In order to compile and run code first clone the repository into your editor and cd into the src folder of the project
```bash
   git clone https://github.com/lillieayer/cs435assignment1.git
   cd yourproject/src
```
### 2. Download all dependencies by running

```bash
 pip install -r requirements.txt
```
## Running the Tool

#### Both the input and output folders are provided as well as all filepaths needed to run the script. 
1. Be sure to empty out the output folder before running the tool by deleting any previous files in the folder.
2. Then run main.py to generate the annotated screenshots which can be found in the output directory in the src directory.

## Purpose

This software tool aims to enhance user understanding of Android graphical user interfaces (GUI) and their hierarchical construction by visually identifying the leaf-level GUI components. This tool will produce a screenshot of a given Android application page with the leaf-level GUI components highlighted with a yellow box. 

### How It Works

This software tool utilizes a python script to process the XML and PNG files representing the GUI components in an Android application. The input comes from the directory Programming-Assignment-Data and contains several screenshots (saved as PNG files) with their corresponding XML file of the same application page. The file names of the PNG and XML files should match with their corresponding pair. This tool will sift through all of the XML files and uses the DOM parser to parse the XML and find all nodes in the file that have no children. After, the PILLOW library is used to help draw on the screenshots using the coordinates specified by the leaf node attribute “bounds.” If there are any bugs present in the XML files then the user is notified and an output screenshot is not generated for that file to ease running the tool. 

### Libraries Used
   - xml.dom.minidom --> for parsing the XML files
   - PIL --> for opening and drawing onto the PNG files
   - os --> for accessing the relevant directories to retrieve XML and PNG files
   - re --> for creating regular expressions to identify patterns in XML
