import unittest

from split_delimiter import split_nodes_delimiter
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

if __name__ == "__main__":
    unittest.main()
        
