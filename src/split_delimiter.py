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

def split_nodes_image(old_nodes):
    return_image_node = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            return_image_node.append(node)
            continue
        original_text = node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            return_image_node.append(node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                return_image_node.append(TextNode(sections[0], TextType.TEXT))
            return_image_node.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            return_image_node.append(TextNode(original_text, TextType.TEXT))
    return return_image_node


def split_nodes_link(old_nodes):
    return_image_node = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            return_image_node.append(node)
            continue
        original_text = node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            return_image_node.append(node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                return_image_node.append(TextNode(sections[0], TextType.TEXT))
            return_image_node.append(
                TextNode(
                    link[0],
                    TextType.LINK,
                    link[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            return_image_node.append(TextNode(original_text, TextType.TEXT))
    return return_image_node

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches
   
def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches
    
def text_to_textnodes(text):
    text = [TextNode(text, TextType.TEXT)]
    text = split_nodes_delimiter(text, "**", TextType.BOLD)
    text = split_nodes_delimiter(text, "*", TextType.ITALIC)
    text = split_nodes_delimiter(text, "`", TextType.CODE)
    text = split_nodes_image(text)
    text = split_nodes_link(text)
    return text
