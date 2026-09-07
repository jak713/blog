from blocktype import BlockType, block_to_block_type, block_to_text, get_num_of_hashes
from leafnode import LeafNode
from markdown_to_blocks import markdown_to_blocks
from parentnode import ParentNode
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node


def markdown_to_html_node(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown) # blocks is just a list of markdown strings, formatting intact
    nodes = []

    for block in blocks:
        blocktype = block_to_block_type(block)
        text = block_to_text(block, blocktype)
        match blocktype:
            case BlockType.CODE:
                children = [LeafNode(value=text, tag=None)]
            case BlockType.ORDERED_LIST:
                children = list_to_children(text)
            case BlockType.UNORDERED_LIST:
                children = list_to_children(text)
            case _:
                children = text_to_children(text)
        if blocktype == BlockType.HEADING:
            heading_hash_number = get_num_of_hashes(block)
            node = children_to_parent(children, blocktype, heading_hash_number)
        else:
           node = children_to_parent(children, blocktype)
        nodes.append(node)

    parentnode = ParentNode(children=nodes, tag="div")

    return parentnode


def text_to_children(text:str) -> list[LeafNode]:
    # the text comes as a string, with a block type associated  of: paragraph, heading, code, quote, u-list and o-list.
    # Leaves should be first, since they are the children
    children = []
    raw_children = text_to_textnodes(text)
    for child in raw_children:
        child = text_node_to_html_node(child)
        children.append(child)
    return children

def children_to_parent(children: list, blocktype: BlockType, num_hashes:int=0) -> ParentNode:
    # Takes the list of children and wraps it in an appropriate block type tag
    match blocktype:
        case BlockType.PARAGRAPH:
            return ParentNode(children=children, tag="p")
        case BlockType.HEADING:
            return ParentNode(children=children, tag=f"h{num_hashes}")
        case BlockType.CODE:
            inside = ParentNode(children=children, tag="code")
            return ParentNode(children=[inside], tag="pre")
        case BlockType.QUOTE:
            return ParentNode(children=children, tag="blockquote")
        case BlockType.UNORDERED_LIST:
            return ParentNode(children=children, tag="ul")
        case BlockType.ORDERED_LIST:
            return ParentNode(children=children, tag="ol")

def list_to_children(text:str) -> list[ParentNode | LeafNode]:
    lines = text.split("\n")
    children = []
    for line in lines:
        sub_children = text_to_children(line)
        if sub_children:
            line = ParentNode(children=sub_children, tag="li")
        else:
            line = LeafNode(value=line, tag="li")
        children.append(line)
    return children
