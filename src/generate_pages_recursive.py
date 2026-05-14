from pathlib import Path
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dir_path_content = Path(dir_path_content)
    template_path = Path(template_path)
    dest_dir_path = Path(dest_dir_path)

    dest_dir_path.mkdir(parents=True, exist_ok=True)

    for item in dir_path_content.iterdir():
        if item.is_dir():
            generate_pages_recursive(
                item,
                template_path,
                dest_dir_path / item.name
            )
        elif item.is_file() and item.suffix == ".md":
            generate_page(
                item,
                template_path,
                dest_dir_path / "index.html"
            )
