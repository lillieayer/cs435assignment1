
from xml.dom.minidom import parse
from PIL import Image, ImageDraw, ImageFont
import os

def get_all_leafs_nodes(allNodes):
    leaves_bounds = []
    for node in allNodes:
        if not node.hasChildNodes():
            leaves_bounds.append(node)
    return leaves_bounds

if __name__ == "__main__":
    # go through provided data directory
    currdir = os.getcwd()
    for file in os.listdir(currdir + "/Programming-Assignment-Data"):
        if file.endswith(".xml"):
            filename = file.split(".xml")[0]
            try:
                # use xml parser to read xml file
                dom = parse(file)
                screenshot = Image.open(filename + ".png")
                # get drawing object to write on screenshot
                canvas = ImageDraw.Draw(screenshot)
                allLeafs = get_all_leafs_nodes(dom.getElementsByTagName("*"))
                for leaf in allLeafs:
                    # get coordinates for leaf components
                    currBound = leaf.getAttribute("bounds")
                    # format into just #
                    currBound = currBound.split("[")
                    print(currBound)
                    canvas.rectangle(((x0,y0), (x1,y1)), outline="yellow", width=3)
                    # save in output folder
                    screenshot.save(currdir + "/output/annotated_" + filename +".png")
            except:
                print("Error parsing file! please fix in file: " + file)
            break
'''