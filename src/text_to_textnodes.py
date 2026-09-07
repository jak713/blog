from split_node import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

def text_to_textnodes(text) -> list[TextNode]:
    nodes = [TextNode(text, TextType.TEXT)]

    # Extract things whose contents shouldn't be parsed for emphasis
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    delimiters = {
        "$": TextType.LATEX,
        "`": TextType.CODE,
        "**": TextType.BOLD,
        "_": TextType.ITALIC,
    }

    for d, t in delimiters.items():
        nodes = split_nodes_delimiter(nodes, d, t)

    return nodes
