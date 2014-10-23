import sys
import glob

INPUT_DIR = "/Users/ben/Desktop/nsf/raw"
OUTPUT_DIR = "/Users/ben/Desktop/nsf/compsci"

TARGET = "Comp/IS/Eng"
TARGET = "COMPUTER"

def run():
    # for input_fname in glob.glob("%s/*" % INPUT_DIR):
    for input_fname in ["%s/%s" % (INPUT_DIR, "Awards-2004.tab")]:
        print("Processing file %s..." % input_fname)
        output_fname = "%s/%s" % (OUTPUT_DIR, input_fname.rsplit("/", 1)[-1])
        with open(input_fname, "r") as f:
            with open(output_fname, "w") as g:
                for line in f:
                    if TARGET in line:
                        g.write(line)
        print("Finished writing file %s..." % output_fname)
    
if __name__ == "__main__":
    run()    
