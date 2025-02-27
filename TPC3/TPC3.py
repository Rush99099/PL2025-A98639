import re
import os

def convert_headers(markdown):
    markdown = re.sub(r'^# (.*)$', r'<h1>\1</h1>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^## (.*)$', r'<h2>\1</h2>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^### (.*)$', r'<h3>\1</h3>', markdown, flags=re.MULTILINE)
    return markdown

def convert_bold(markdown):
    return re.sub(r'\*\*(.*)\*\*', r'<b>\1</b>', markdown)

def convert_italic(markdown):
    return re.sub(r'\*(.*)\*', r'<i>\1</i>', markdown)

def convert_numered_lists(markdown):
    lines = markdown.split('\n')
    in_list = False
    result = []
    for line in lines:
        if re.match(r'^\d+\.', line):
            if not in_list:
                result.append('<ol>')
                in_list = True
            result.append(re.sub(r'^\d+\.\s*(.*)$', r'<li>\1</li>', line))
        else:
            if in_list:
                result.append('</ol>')
                in_list = False
            result.append(line)
    if in_list:
        result.append('</ol>')
    return '\n'.join(result)
    
def convert_links(markdown):
    return re.sub(r'\[(.*)\]\((.*)\)', r'<a href="\2">\1</a>', markdown)

def convert_images(markdown):
    return re.sub(r'!\[(.*)\]\((.*)\)', r'<img src="\2" alt="\1">', markdown)

def markdown_to_html(markdown):
    markdown = convert_headers(markdown)
    markdown = convert_bold(markdown)
    markdown = convert_italic(markdown)
    markdown = convert_numered_lists(markdown)
    markdown = convert_images(markdown)
    markdown = convert_links(markdown)
    return markdown

def convert_md_to_html(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"File {input_file} not found.")
        return
    with open(input_file, 'r') as file:
        markdown = file.read()
    html = markdown_to_html(markdown)
    with open(output_file, 'w') as file:
        file.write(html)

# Convert input.txt to output.html
convert_md_to_html('c:/Users/bruno/Desktop/Uni/2sem/PL/PL2025-A98639/TPC3/input.md', 'c:/Users/bruno/Desktop/Uni/2sem/PL/PL2025-A98639/TPC3/output.html')