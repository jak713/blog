from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag:str, children:list[object], props:dict|None=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("parent node must have a tag")
        if self.children is None or len(self.children) == 0:
            raise ValueError("parent node must have children")

        children_html = ""

        for child in self.children:
            children_html += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
