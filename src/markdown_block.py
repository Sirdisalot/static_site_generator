block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "unordered list"
block_type_olist = "ordered list"

def markdown_to_blocks(markdown):
    inline_markdown = markdown.split("\n")
    return_value = []
    for i in range(len(inline_markdown)):
        if inline_markdown[i] != "":
            return_value.append(inline_markdown[i].lstrip())
    for i in range(len(return_value)):
        if return_value[i] == "":
            return_value.pop(i)
    return return_value

def block_to_block_type(block):
    lines = block.split("\n")
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return block_type_heading
    if block.startswith("```") and block.endswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
            return block_type_quote
        return block_type_quote
    if block.startswith(("* ", "- ")):
        for line in lines:
            if not line.startswith(("* ", "- ")):
                return block_type_paragraph
            return block_type_ulist
        return block_type_ulist
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist
    else:
        return block_type_paragraph

block_to_block_type("## heading")
