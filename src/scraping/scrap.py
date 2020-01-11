import src.utils as ut

import sys
import json 

def main():
    args = sys.argv
    project_params = json.load(open(args[1]))
    scrap_params = json.load(open(args[2]))


if __name__ == "__main__":
    main()