from textnode import TextNode, TextType

def main():
    node1 = TextNode(TextType.BOLD, "This is some anchor text", 'https://bootdev.com')
    print(node1)

if __name__ == "__main__":
    main()