from textnode import TextType, TextNode
from text_to_html import text_node_to_html_node
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if delimiter == None:
        raise Exception("That is an invalid Markdown syntax")
    return_text_node = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            return_text_node.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdwon, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        return_text_node.extend(split_nodes)
    return return_text_node

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches
   
def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches
    
    