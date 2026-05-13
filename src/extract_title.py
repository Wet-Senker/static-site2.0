def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("#"):
            return line.split("#")[1].strip()
    raise ValueError("Document doesn't contain #") 

markdown = "# Hello how are you?"

print(extract_title(markdown))

"""
For the next step, adjust your condition so it matches lines like:

# Title

but does not match:

## Subtitle

Hint: after confirming the line starts with #, what should the next character usually be for an h1 written in normal markdown?
"""