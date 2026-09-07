def markdown_to_blocks(markdown: str) -> list[str]:
    lines = markdown.splitlines()
    blocks = []
    current_block = []
    in_code_block = False

    for line in lines:
        if line.startswith("```"):
            in_code_block = not in_code_block
            current_block.append(line)
            continue

        if not in_code_block and line.strip() == "":
            if current_block:
                blocks.append("\n".join(current_block).strip())
                current_block = []
        else:
            current_block.append(line)

    if current_block:
        blocks.append("\n".join(current_block).strip())

    return blocks
