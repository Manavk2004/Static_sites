from textnode import TextType, TextNode

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    def props_to_html(self):
        if self.props is None:
            return ""
        str = ''
        for i in self.props:
            str += f" {i}='{self.props[i]}'"
        return str
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("No value")
        if self.tag is None:
            return self.value
        if self.tag == "img":
            return f"<{self.tag}{self.props_to_html()}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("There is no tag")
        if self.children is None:
            raise ValueError("There is a value missing in children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f'<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>'


def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
       new_leafnode = LeafNode(None, text_node.text)
       return new_leafnode
    if text_node.text_type == TextType.BOLD:
        new_leadnode = LeafNode("b", text_node.text)
        return new_leafnode
    if text_node.text_type == TextType.ITALIC:
        new_leafnode = LeafNode("i", text_node.text)
        return new_leafnode
    if text_node.text_type == TextType.CODE:
        new_leafnode = LeafNode("code", text_node.text)
        return new_leafnode
    if text_node.text_type == TextType.LINK:
        new_leafnode = LeafNode("a", text_node.text)
        return new_leafnode
    if text_node.text_type == TextType.IMAGE:
        new_leafnode = LeafNode("img", "", props={"src": text_node.url, "alt": text_node.text})
        return new_leafnode
    else:
        raise Exception("Invalid text type")