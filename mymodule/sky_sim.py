"""
A script to simulate a population of stars around the Andromeda galaxy.
"""

import math
import random


NSRC = 1_000_000

def get_radec():

    """
    This function is to determine the location of Andromeda in ra/dec (degrees).
    For this function, values for the RA and Dec of Andromeda from Wikipedia
    are given, and are converted to degrees. 
    """

    # assign RA and Dec a constant value (for now) from wikipedia
    RA = '00:42:44.3'
    DEC = '41:16:09'

    # convert to decimal degrees
    d, m, s = DEC.split(':')
    dec = int(d)+int(m)/60+float(s)/3600

    h, m, s = RA.split(':')
    ra = 15*(int(h)+int(m)/60+float(s)/3600)
    ra = ra/math.cos(dec*math.pi/180)
    
    return (ra, dec)



def make_stars(ra:float, dec:float, num_stars:int) -> tuple(List(float),List(float)):
    """
    Make 1000 stars within 1 degree of Andromeda
    """
    ras = []
    decs = []
    for i in range(NSRC):
        ras.append(ra + random.uniform(-1,1))
        decs.append(dec + random.uniform(-1,1))

    return (ras, decs)


def main():
    ra, dec = get_radec()
    ras, decs = make_stars(ra, dec, NSRC)

    # now write these to a csv file for use by my other program
    with open('catalog.csv','w',encoding='utf-8') as f:
        print("id,ra,dec", file=f)
        for i in range(NSRC):
            print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}", file=f)

if __name__ == '__main__':
    main()
