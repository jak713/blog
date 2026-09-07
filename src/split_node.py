from extract_md import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    nodes = []
    
    for node in old_nodes:
        if node.text_type!=TextType.TEXT:
            nodes.append(node)
            continue
        if node.text.count(delimiter)%2!=0:
            raise Exception(f"closing delimiter for {delimiter} not found in node {node}")

        text = node.text.split(delimiter)
        i = 0
        while i < len(text):
            if text[i] == "":
                i+=1
                continue

            if i%2==0:
                nodes.append(TextNode(text=text[i], text_type=TextType.TEXT))
            else:
                nodes.append(TextNode(text=text[i], text_type=text_type))
            i+=1

    return nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    # extract_markdown_images works on text and extracts the links from the text
    # in [(alt, url)] format
    nodes = []

    for node in old_nodes:
        if node.text_type!=TextType.TEXT:
            nodes.append(node)
            continue

        links = extract_markdown_links(node.text)
        # multiple links may come in list of tuples
        text = node.text
        for link in links:
            text = text.split(f"[{link[0]}]({link[1]})", 1)
            
            if text[0] != "":
                nodes.append(TextNode(text=text[0], text_type=TextType.TEXT))
            nodes.append(TextNode(text=link[0], text_type=TextType.LINK, url=link[1]))
            
            text = text[-1]
        
        if text != "":
            nodes.append(TextNode(text=text, text_type=TextType.TEXT))
    return nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    nodes = []

    for node in old_nodes:
        if node.text_type!=TextType.TEXT:
            nodes.append(node)
            continue

        images = extract_markdown_images(node.text)
        text = node.text

        for image in images:
            text = text.split(f"![{image[0]}]({image[1]})", 1)
            
            if text[0] != "":
                nodes.append(TextNode(text=text[0], text_type=TextType.TEXT))

            nodes.append(TextNode(text=image[0], text_type=TextType.IMAGE, url=image[1]))

            text = text[-1]

        if text != "":
            nodes.append(TextNode(text=text, text_type=TextType.TEXT))

    return nodes

if __name__=="__main__":
    node = TextNode("check [here](url) and again [here](url)", text_type=TextType.TEXT)

    #node = TextNode("text with [link1](url1) and [link2](url2) end", TextType.TEXT)
    new_nodes = split_nodes_link([node])
    print(node.text)
    print(new_nodes)
