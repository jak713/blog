from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'


def block_to_block_type(block: str) -> BlockType:
    if block.startswith('```') and block.endswith('```'):
        return BlockType.CODE
    if '# ' in block[:7]:
        return BlockType.HEADING
    if block[0] == '>':
        return BlockType.QUOTE

    lines = block.split("\n")
    counter = 1

    while counter <= len(lines):
        if counter == len(lines):
            if lines[counter - 1].startswith("- "):
                return BlockType.UNORDERED_LIST

            if lines[counter - 1].startswith(f"{counter}. "):
                return BlockType.ORDERED_LIST

        if not (
            lines[counter - 1].startswith("- ")
            or lines[counter - 1].startswith(f"{counter}. ")
        ):
            break

        counter += 1

    return BlockType.PARAGRAPH

def get_num_of_hashes(block:str) -> int:
        return block[:6].count("#")

def block_to_text(block:str, blocktype:BlockType) -> str:
    match blocktype:
        case BlockType.PARAGRAPH:
            parts = block.split("\n")
            whole = " ".join(parts)
            return whole
    
        case BlockType.HEADING:
            count = block[:6].count("#")
            return block[count+1:]

        case BlockType.QUOTE:
            raw_parts = block.split('\n')
            parts = []
            for part in raw_parts:
                part = part[2:]
                parts.append(part)
            return " ".join(parts)

        case BlockType.UNORDERED_LIST:
            whole = []
            parts = block.split("\n")
            for part in parts:
                part = part[2:]
                whole.append(part)

            text = "\n".join(whole)
            return text

        case BlockType.ORDERED_LIST:
            whole = []
            parts = block.split("\n")
            counter = 1
            for part in parts:
                if counter < 10:
                    part = part[3:]
                else:
                    part = part[4:]
                whole.append(part)

            text = "\n".join(whole)
            return text

        case BlockType.CODE:
            first = block.find('\n')
            return block[first+1:-3]

