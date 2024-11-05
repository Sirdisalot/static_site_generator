import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType
from text_to_html import text_node_to_html_node

class TestTextToHtml(unittest.TestCase):
    def test_text_bold_text_type(self):
        node = TextNode("a", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        expected = "<b>a</b>"
        self.assertEqual(html_node.to_html(), expected)

    def test_text_italic_text_type(self):
        node = TextNode("a", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        expected = "<i>a</i>"
        self.assertEqual(html_node.to_html(), expected)

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()
        