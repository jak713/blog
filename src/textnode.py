from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    LATEX = "latex"


class TextNode:
    def __init__(self, text:str, text_type:TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other) -> bool:
        return all([self.text == other.text, self.text_type == other.text_type, self.url == other.url])

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    value = text_node.text
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=value)
        case TextType.BOLD:
            return LeafNode(tag="b" , value=value)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=value)
        case TextType.CODE:
            return LeafNode(tag="code", value=value)
        case TextType.LINK:
            return LeafNode(tag="a", value=value, props={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode(tag="img", value="", props={"src": text_node.url, "alt":value})
        case TextType.LATEX:
            return LeafNode(tag="span", value=f"${value}$", props={"class":"math"})
        case _:
            raise Exception("Text type does not exist")

