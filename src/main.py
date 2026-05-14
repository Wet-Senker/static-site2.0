from pathlib import Path
from copy_and_delete import copy_and_delete
from generate_pages_recursive import generate_pages_recursive
import sys

working_directory = Path(__file__).parent.parent

src = working_directory / "static"
dst = working_directory / "docs"
content = working_directory / "content"
template = working_directory / "template.html"

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    copy_and_delete(src, dst)
    generate_pages_recursive(content, template, dst, basepath)

main()