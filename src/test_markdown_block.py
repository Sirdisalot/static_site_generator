import unittest

from markdown_block import *


class TestMarkdownBlock(unittest.TestCase):
    def test_markdown_to_blocks(self):
        node = '''
            # This is a heading

            This is a paragraph of text. It has some **bold** and *italic* words inside of it.

            * This is the first list item in a list block
            * This is a list item
            * This is another list item
        '''
        expected = [
            '# This is a heading', 
            'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
            '* This is the first list item in a list block', 
            '* This is a list item', 
            '* This is another list item',
        ]
        print(markdown_to_blocks(node))
        print(f"This is expected: {expected}")
        self.assertEqual(markdown_to_blocks(node), expected)
    
    def test_markdown_block_paragraph(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_ulist)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_olist)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

if __name__ == "__main__":
    unittest.main()