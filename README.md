# Utility Scripts Repository

This repository contains a toolkit of utility scripts for file management, Git operations, and code consolidation.

## Table of Contents
1. [Installation](#installation)
2. [Usage as a Python Package](#usage-as-a-python-package)
3. [Individual Tools](#individual-tools)
   3.1. [remove_newlines: Newline Removal Utility](#newline-removal-utility)
   3.2. [doc_consolidator: File Processing and Code Consolidation Utility](#file-processing-and-code-consolidation-utility)
   3.3. [file_rename: Cross-Platform File Renaming Utility (Jupyter Notebook)](#cross-platform-file-renaming-utility-jupyter-notebook)
   3.4. [flexible_history_rewrite: Git History Rewrite Script](#git-history-rewrite-script)

## Installation

To use this toolkit, clone the repository and install it as a Python package:

```bash
git clone https://github.com/your-username/utility-scripts-repo.git
cd utility-scripts-repo
pip install -e .
```

## Usage as a Python Package

After installation, you can use the toolkit in your Python scripts as follows:

```python
from toolkit import remove_newlines, consolidate_code

# Use remove_newlines
remove_newlines('input.txt', 'output.txt')

# Use consolidate_code
consolidate_code('/path/to/project', ['.py', '.js'], 'consolidated_code.txt')
```

## Individual Tools

### Newline Removal Utility

**Function**: `remove_newlines(input_filename, output_filename=None)`

This utility removes unnecessary newlines from text files, consolidating paragraphs while preserving intentional line breaks between paragraphs.

#### Usage
```python
python remove_newlines.py <input_filename> [<output_filename>]
```

If no output filename is provided, the input file will be overwritten with the processed text.

#### Notes
- This script is useful for cleaning up text files with excessive line breaks, such as those copied from PDFs or web pages.
- It preserves paragraph structure by maintaining double line breaks between paragraphs.

### File Processing and Code Consolidation Utility

**File**: `doc_consolidator.py`

This utility consolidates code files of specified extensions into a single file for analysis.

#### Key features:
- Recursive file processing in a directory and its subdirectories
- Support for multiple file extensions
- Exclusion of specified folders
- Safe file reading with multiple encoding attempts

#### Usage

You can use this utility in two ways:

1. As a Python function:

```python
from doc_consolidator import consolidate_code

output_file = consolidate_code(
    root_path='/path/to/your/project',
    extensions=['.py', '.js', '.html'],
    output_filename='consolidated_code.txt'
)
print(f"Consolidated code saved to: {output_file}")
```

2. Directly from the command line:

```bash
python3 doc_consolidator.py /path/to/project '.py,.js' output.txt
```

This command will consolidate all `.py` and `.js` files in the `/path/to/project` directory (and its subdirectories) into a file named `output.txt`.

If you omit the output filename, a default name will be generated based on the current date.

#### Notes:
- By default, the following folders are excluded from processing: "ss", "myenv", "__pycache__", ".git", "node_modules". You can modify this list in the `consolidate_code` function if needed.
- When using the command-line interface, these default exclusions are applied and cannot be modified without changing the script.

### Cross-Platform File Renaming Utility (Jupyter Notebook)

**File**: `file_rename.ipynb`

This Jupyter notebook contains a function `rename_fn(folder_path, old_string, new_string)` for batch renaming files in a directory and its subdirectories.

#### Key features:
- Recursive file renaming in a directory and its subdirectories
- Cross-platform compatibility (Windows, Mac, Linux)
- Handling of special characters in file names
- File conflict resolution with user prompts
- File size comparison for conflict resolution
- Option to keep both files by appending numbers to filenames

#### Usage
To use it, open the notebook in Jupyter, run all cells to define the function, then use it as follows:

```python
# For Mac/Linux:
rename_fn('/Volumes/', 'video - ', '')

# For Windows:
rename_fn(r'C:\Program Files\My Folder', 'old-', 'new-')
```

### Git History Rewrite Script

**File**: `flexible_history_rewrite.sh`

This Bash script provides a way to interactively rebase and rewrite the entire Git history of a repository.

#### Key features:
- Automatic detection of total commit count
- Interactive rebase from the root of the repository
- Force push to update remote repository
- Cleanup of refs and aggressive garbage collection

#### Usage
Run it from the command line in your Git repository:

```bash
./flexible_history_rewrite.sh
```

#### Caution
This script rewrites Git history and force pushes the changes. Use with extreme caution, especially on shared repositories. It's recommended to create a backup branch before running this script:
```
git checkout -b backup_branch
git checkout main
```

Always communicate with your team before using this on a shared repository, as it can cause issues for other contributors.

## Notes

- The toolkit contains a mix of Python scripts, a shell script, and a Jupyter notebook.
- Always ensure you have backups before using these utilities, especially when modifying files or Git history.
- For detailed usage instructions for each tool, refer to the respective sections above or the comments in the source files.