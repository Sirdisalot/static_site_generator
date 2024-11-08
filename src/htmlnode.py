class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    
    def props_to_html(self):
        props_string = []
        if self.props == None:
            return ""
        else:
            for k, v in self.props.items():
                temp_props_string = f' {k}="{v}"'
                props_string.append(temp_props_string)
        return "".join(props_string)
    
    def __repr__(self):
        return f"""HTMLNode(
        tag={self.tag},
        value={self.value},
        children={self.children},
        props={self.props},
        )"""

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def add_child(self):
        raise ValueError("LeafNode cannot have children.")
    
    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Must have a tag")
        if self.children is None:
            raise ValueError("Must have children")
        child_string = []
        for child in self.children:
            child_string.append(child.to_html())
        children_html = "".join(child_string)
        complete_html = f"<{self.tag}>{children_html}</{self.tag}>"
        return complete_html        
        
