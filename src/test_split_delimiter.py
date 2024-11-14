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
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_markdown_links(self):
        node = TextNode(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.LINK, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )
    

if __name__ == "__main__":
    unittest.main()