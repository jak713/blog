from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag:str|None, value:str, props:dict|None=None):
        super().__init__(value=value, tag=tag, children=None, props=props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("leaf node must have a value")
        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode:\nTag: {self.tag}\nValue: {self.value}\nProps: {self.props}"

