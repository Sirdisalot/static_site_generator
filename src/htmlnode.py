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
