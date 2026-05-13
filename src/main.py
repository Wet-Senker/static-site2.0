from pathlib import Path
from copy_and_delete import copy_and_delete
from generate_page import generate_page

working_directory = Path(__file__).parent.parent

src = working_directory / "static"
dst = working_directory / "public"

pages_content = ["content/blog/glorfindel/index.md", "content/blog/tom/index.md", "content/blog/majesty/index.md", "content/contact/index.md"]

pages_public = ["public/blog/glorfindel/index.md", "public/blog/tom/index.md", "public/blog/majesty/index.md", "public/contact/index.md"]

def main():
    copy_and_delete(src, dst)
    for page_content, page_public in zip(pages_content, pages_public):
        generate_page(page_content, "template.html", page_public)
        
main()