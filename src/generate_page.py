from pathlib import Path
from markdown_blocks import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path):
    from_path = Path(from_path)
    template_path = Path(template_path)
    dest_path = Path(dest_path)

    print(f"Generating from {from_path} to {dest_path} using {template_path}")

    content_fp = from_path.read_text()
    content_tp = template_path.read_text()

    mark_html = markdown_to_html_node(content_fp)
    html = mark_html.to_html()
    title = extract_title(content_fp)

    new_html = content_tp.replace("{{ Title }}", title)
    new_html = new_html.replace("{{ Content }}", html)

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    dest_path.write_text(new_html)
