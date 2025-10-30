def markdown_to_blocks(markdown):
    filtered_blocks = []
    blocks = markdown.split('\n\n')
    for block in blocks:
        if block == '':
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks