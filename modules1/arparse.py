import argparse
import math

parser = argparse.ArgumentParser(description="Volume of cylinder")
parser.add_argument('rad', type=int, help="Radius of cylinder")
parser.add_argument('ht', type=int, help="Height of cylinder")
args = parser.parse_args()


def cylvol(rad,ht):
    vol = (math.pi) * (rad**2)*ht
    return vol

print(cylvol(args.rad, args.ht))
