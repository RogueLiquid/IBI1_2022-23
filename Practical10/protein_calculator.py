#use re to locate the "ATG" and "TGA"
#calculate the length betweem condons
#calculate the proportion of length in the whole sequence
import re
DNA = "ATGGGGTTTTTTTCCCCCCAAAAATTTTGAAAAACCCTTTTTTGGGGGGG"

def PC_calculate(DNA):
    locate_ATG = re.search("ATG",DNA)
    locate_TGA = re.search("TGA",DNA)
    location_ATG = re.findall("span=.(\d+)",str(locate_ATG))
    location_TGA = re.findall("span=.(\d+)",str(locate_TGA))
    length = int(location_TGA[0]) - int(location_ATG[0])
    total = len(DNA)
    if length > 0.5*total:
        print("protein-coding")
    elif length < 0.1*total:
        print("non-coding")
    else:
        print("unclear")
        
PC_calculate(DNA)