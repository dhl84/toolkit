import os
import shutil
from datetime import datetime, timezone
import re
from typing import Union, List
import sys

def read_file_safe(file_path):
    encodings = ['utf-8', 'latin-1', 'ascii', 'utf-16']
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return file.read()
        except UnicodeDecodeError:
            continue
    print(f"Warning: Unable to read {file_path} with any of the attempted encodings.")
    return f"[Error: Could not read file {file_path} due to encoding issues]"

def process_files(task: str, root_path: str = None, extensions: Union[str, List[str]] = None, 
                  output_filename: str = None, exclude_folders: List[str] = ["ss", "myenv", "__pycache__", ".git", "node_modules"]):
    """
    A versatile function to handle file processing tasks including concatenation, 
    file structure generation, and backup operations.

    Args:
    task (str): The task to perform ('concatenate', 'structure', 'backup')
    root_path (str): The root directory path (default: two levels up from current directory)
    extensions (str or List[str]): File extension(s) to process (for 'concatenate' task)
    output_filename (str): Name of the output file
    exclude_folders (List[str]): Folders to exclude from processing

    Returns:
    str: Path to the output file
    """
    def clean_ansi(text):
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        return ansi_escape.sub('', text)

    if root_path is None:
        root_path = os.path.abspath(os.path.join(os.getcwd(), '..', '..'))

    if output_filename is None:
        output_filename = f"{task}_{datetime.now(timezone.utc).strftime('%d%b%y')}.txt"

    output_path = os.path.join(os.getcwd(), output_filename)
    
    ss_folder = os.path.join(os.getcwd(), "ss")
    os.makedirs(ss_folder, exist_ok=True)

    temp_output_path = output_path + '.temp'

    with open(temp_output_path, 'w', encoding='utf-8') as outfile:
        current_time = datetime.now(timezone.utc)
        outfile.write(f"Filename: {output_filename}\n")
        outfile.write(f"Generated on: {current_time.strftime('%Y-%m-%d %H:%M:%S')} UTC\n\n")
        
        if task == 'concatenate':
            if isinstance(extensions, str):
                extensions = [extensions]
            extensions = ['.' + ext.lstrip('.') for ext in extensions]

            for dirpath, dirnames, filenames in os.walk(root_path):
                dirnames[:] = [d for d in dirnames if d not in exclude_folders]
                for filename in filenames:
                    if any(filename.endswith(ext) for ext in extensions):
                        file_path = os.path.join(dirpath, filename)
                        relative_path = os.path.relpath(file_path, root_path)
                        outfile.write(f"--- Content of {relative_path} ---\n\n")
                        file_content = read_file_safe(file_path)
                        outfile.write(file_content)
                        outfile.write("\n\n")

        elif task == 'structure':
            for dirpath, dirnames, filenames in os.walk(root_path):
                dirnames[:] = [d for d in dirnames if d not in exclude_folders]
                level = dirpath.replace(root_path, '').count(os.sep)
                indent = '  ' * level
                outfile.write(f"{indent}{os.path.basename(dirpath)}/\n")
                for f in filenames:
                    outfile.write(f"{indent}  {f}\n")

        elif task == 'backup':
            ss_folder = os.path.join(root_path, 'ss')
            os.makedirs(ss_folder, exist_ok=True)
            
            root_files = [f for f in os.listdir(root_path) if os.path.isfile(os.path.join(root_path, f))]
            today = datetime.now().strftime("%d%b%y")
            
            for file in root_files:
                if file == 'analysis' or file.startswith('.'):
                    continue
                
                root_file_path = os.path.join(root_path, file)
                file_name, file_ext = os.path.splitext(file)
                
                ss_files = [f for f in os.listdir(ss_folder) if f.startswith(file_name)]
                most_recent = max(ss_files, key=lambda f: os.path.getmtime(os.path.join(ss_folder, f)), default=None)
                
                if most_recent:
                    most_recent_path = os.path.join(ss_folder, most_recent)
                    if os.path.getmtime(root_file_path) > os.path.getmtime(most_recent_path):
                        new_file_name = f"{file_name}_{today}{file_ext}"
                        shutil.copy2(root_file_path, os.path.join(ss_folder, new_file_name))
                        outfile.write(f"Backed up {file} to {new_file_name}\n")
                else:
                    new_file_name = f"{file_name}_{today}{file_ext}"
                    shutil.copy2(root_file_path, os.path.join(ss_folder, new_file_name))
                    outfile.write(f"Backed up {file} to {new_file_name}\n")

    if os.path.exists(output_path):
        with open(output_path, 'r', encoding='utf-8') as f1, open(temp_output_path, 'r', encoding='utf-8') as f2:
            if f1.read() != f2.read():
                backup_time = datetime.now()
                backup_filename = f"{os.path.splitext(output_filename)[0]}_{backup_time.strftime('%d%b%y_%H%M')}.txt"
                backup_path = os.path.join(ss_folder, backup_filename)
                shutil.move(output_path, backup_path)
                print(f"Created backup: {backup_path}")
                
                os.rename(temp_output_path, output_path)
                print(f"Updated: {output_path}")
            else:
                os.remove(temp_output_path)
                print(f"No changes detected. Keeping existing file. [{output_filename}]")
    else:
        os.rename(temp_output_path, output_path)
        print(f"Created new file: {output_path}")

    return output_path

def consolidate_code(root_path: str, extensions: Union[str, List[str]], output_filename: str = None, 
                     exclude_folders: List[str] = ["ss", "myenv", "__pycache__", ".git", "node_modules"]):
    """
    Consolidate code files of specified extensions into a single file for analysis.

    Args:
    root_path (str): The root directory path to search for files
    extensions (str or List[str]): File extension(s) to process
    output_filename (str): Name of the output file (default: 'consolidated_code_{date}.txt')
    exclude_folders (List[str]): Folders to exclude from processing

    Returns:
    str: Path to the output file
    """
    if output_filename is None:
        output_filename = f"consolidated_code_{datetime.now(timezone.utc).strftime('%d%b%y')}.txt"

    return process_files('concatenate', root_path, extensions, output_filename, exclude_folders)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 doc_consolidator.py <root_path> <extensions> [output_filename]")
        print("Example: python3 doc_consolidator.py /path/to/project '.py,.js' output.txt")
        sys.exit(1)

    root_path = sys.argv[1]
    extensions = sys.argv[2].split(',')
    output_filename = sys.argv[3] if len(sys.argv) > 3 else None

    result = consolidate_code(root_path, extensions, output_filename)
    print(f"Consolidated code saved to: {result}")