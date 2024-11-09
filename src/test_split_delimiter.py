import unittest

from split_delimiter import *
from textnode import TextNode, TextType

class TestSplitDelimiter(unittest.TestCase):
    def test_textnode_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        expected = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" word", TextType.TEXT),
],
            expected
        )

    def test_textnode_bold(self):
        node = TextNode("This is text with a **code block** word", TextType.TEXT)
        expected = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("code block", TextType.BOLD),
    TextNode(" word", TextType.TEXT),
],
            expected
        )

    def test_double_bold(self):
        node = TextNode("This is **text** with a **code block** word", TextType.TEXT)
        expected = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
    TextNode("This is ", TextType.TEXT),
    TextNode("text", TextType.BOLD),
    TextNode(" with a ", TextType.TEXT),
    TextNode("code block", TextType.BOLD),
    TextNode(" word", TextType.TEXT),
],
            expected
        )

    def test_italic(self):
        node = TextNode("This is text with a *code block* word", TextType.TEXT)
        expected = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("code block", TextType.ITALIC),
    TextNode(" word", TextType.TEXT),
],
            expected
        )

    def test_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extract_markdown_links(text), expected)
    

if __name__ == "__main__":
    unittest.main()
        
