import sys
from make_public_dir import make_public_dir
from generation_utils import generate_pages_recursive

def main(basepath):
    make_public_dir()
    generate_pages_recursive("content/", "template.html", "docs/", basepath)

if __name__ == "__main__":
    basepath = "/"
    if len(sys.argv)>=2:
        basepath = sys.argv[1]

    main(basepath)
