from pathlib import Path
from copy_and_delete import copy_and_delete

working_directory = Path(__file__).parent.parent

src = working_directory / "static"
dst = working_directory / "public"

def main():
    copy_and_delete(src, dst)
        
main()