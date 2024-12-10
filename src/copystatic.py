import os
import shutil
from markdown_block import markdown_to_html_node
from pathlib import Path

def copy_file_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_file_recursive(from_path, dest_path)


def extract_title(markdown):
    if markdown.startswith("# "):
        return markdown.lstrip("# ")
    else:
        raise Exception("No title found")
    
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()
    
    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    html = markdown_to_html_node(markdown_content).to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)
