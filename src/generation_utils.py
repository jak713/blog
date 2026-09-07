import os
from os.path import isfile
from markdown_to_html_node import markdown_to_html_node

def extract_title(markdown:str) -> str:
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()
    raise NoTitleError("No title found.")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        md = file.read()

    with open(template_path, "r") as file:
        template = file.read()

    content = markdown_to_html_node(md).to_html()
    title = extract_title(md)
    
    template = template.replace("{{ Content }}", content)
    template = template.replace("{{ Title }}", title)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))

    with open(dest_path, "w") as file:
        file.write(template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    files = os.listdir(dir_path_content)
    for file in files:
        from_path = os.path.join(dir_path_content, file)
        if os.path.isfile(from_path) and file.endswith(".md"):
            to_path = os.path.join(dest_dir_path, file.replace(".md", ".html"))
            generate_page(from_path=from_path, template_path=template_path, dest_path=to_path, basepath=basepath)
        elif os.path.isdir(from_path):
            to_path = os.path.join(dest_dir_path, file)
            generate_pages_recursive(from_path, template_path, to_path, basepath)


class NoTitleError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
