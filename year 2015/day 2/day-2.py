import sys
import os
import re

if __name__ == "__main__":

    paper = 0
    ribbon = 0
    fp = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(fp, "data.txt"), "r") as file:
        
     for line in file:
        a = re.search("(\d{1,3})x(\d{1,3})x(\d{1,3})", line)
    
        b = int(a.group(1))
        c = int(a.group(2))
        d = int(a.group(3))

        sides = [a, b, c]
        perims = [2*a + 2*b, 2*b + 2*c,2*c + 2*a]
    
        sides.sort()
        perims.sort()
    
        slack = sides[0] * sides[1]
    
        paper += 2*(a*b) + 2*(b*c) + 2*(c*a) + slack
        ribbon += (a*b*c) + perims[0]
    
print (paper)
print (ribbon)