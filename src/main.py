from textnode import TextNode, TextType

def main():
    node1 = TextNode(TextType.BOLD_TEXT, "This is some anchor text", 'https://bootdev.com')
    print(node1)

if __name__ == "__main__":
    main()