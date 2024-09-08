import sys
import os

def generate_file_with_content(file_path, add_content, need_content):
    """
    Generate a file with content if the file does not exist or the content is not in the file.
    """
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            content = f.read()
        if need_content not in content:
            with open(file_path, "a") as f:
                f.write(f"\n{add_content}\n")
            print(f"Add `{add_content}` to the {file_path} file.")
        else:
            print(f"The `{need_content}` is already in the {file_path} file.")
    else:
        with open(file_path, "w") as f:
            f.write(f"\n{add_content}\n")
        print(f"Add `{add_content}` to the {file_path} file.")

def generate_openai_env():
    generate_file_with_content(".gitignore", ".env", ".env")
    generate_file_with_content(".env", "OPENAI_API_KEY=<YOUR-OPENAI_API_KEY>", "OPENAI_API_KEY")