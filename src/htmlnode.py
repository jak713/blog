from types import NotImplementedType


class HTMLNode:
    def __init__(self, tag:str|None=None, value:str|None=None, children:list[object]|None=None, props:dict|None=None):
        self.tag = tag 
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props:
            return " " + " ".join([f'{k}="{v}"' for k, v in self.props.items()])
        return ""

    def __repr__(self) -> str:
        return f"HTMLNode:\nTag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProps: {self.props}"
