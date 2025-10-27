from enum import Enum

class TextType(Enum):
    TEXT = 'text'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    image = 'image'

class TextNode:
    def __init__(self, text_type, text, url=None):
        self.text_type = text_type
        self.text = text
        self.url = url
    
    def __eq__(self, other):
        if self.text_type == other.text_type and self.text == other.text and self.url == other.url:
            return True
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


