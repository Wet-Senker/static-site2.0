from markdown_blocks import markdown_to_html_node
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating from {from_path} to {dest_path} using {template_path}")

    with open (from_path, "r") as f:
        content_fp = f.read()
        
    with open(template_path) as f:
        content_tp = f.read()
        
    mark_html = markdown_to_html_node(content_fp)
    html = mark_html.to_html()
    
    title = extract_title(content_fp)

    new_html = content_tp.replace("{{ Title }}", title)
    new_html = new_html.replace("{{ Content }}", html)
    
    if not os.path.exists(dest_path):
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        
    with open(dest_path, 'w') as f:
        dest_path = f.write(new_html)