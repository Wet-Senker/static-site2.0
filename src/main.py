from pathlib import Path
from copy_and_delete import copy_and_delete
from generate_pages_recursive import generate_pages_recursive

working_directory = Path(__file__).parent.parent

src = working_directory / "static"
dst = working_directory / "public"
content = working_directory / "content"
template = working_directory / "template.html"

def main():
    copy_and_delete(src, dst)
    generate_pages_recursive(content, template, dst)

main()
