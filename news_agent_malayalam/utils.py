import os

def load_instruction(filename='instruction.txt') -> str:
    base_dir = os.path.dirname(os.path.abspath(__file__))  # path to the current file
    file_path = os.path.join(base_dir, filename)


    if not os.path.exists(file_path):
        raise Exception(f"Instruction file not found at: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
