# perso
import src.utils as ut

# system
import sys
import json 

# external
import scrapy

def main():
    args = sys.argv
    project_params = json.load(open(args[1]))
    scrap_params = json.load(open(args[2]))


if __name__ == "__main__":
    main()