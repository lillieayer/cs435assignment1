# CS435 Assignment 1

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
1. Be sure to empty out the output folder before running the tool. Then run main.py to generate the annotated screenshots which can be found in the output directory in the src directory.

## Description

#### My solution essentially includes all the input and output folders and then will sift through all of the xml files and uses the DOM parser to parse the xml and find all nodes in the file that have no children. After, the PILLOW library is used to help draw on the screenshots using the coordinates specified by the leaf node attribute “bounds.” I chose to make running the tool easy for the user and if any bugs come up in the files then the user is notified and a screenshot is just not generated for that file to ease running the tool. 
