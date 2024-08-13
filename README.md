# Utility Scripts Repository

This repository contains two utility scripts for file management and Git operations.

## Table of Contents
1. [file_rename.ipynb: Cross-Platform File Renaming Utility (Jupyter Notebook)](#1-cross-platform-file-renaming-utility-jupyter-notebook)
2. [flexible_history_rewrite.sh: Git History Rewrite Script](#2-git-history-rewrite-script)
3. [doc_consolidator.py: File Processing and Code Consolidation Utility](#3-file-processing-and-code-consolidation-utility)
4. [remove_newlines.py: Newline Removal Utility](#4-newline-removal-utility)

## 1. Cross-Platform File Renaming Utility (Jupyter Notebook)

**Filename**: `file_rename.ipynb`

### Description

This utility is provided as a Jupyter notebook containing a robust, cross-platform function for renaming files within a specified directory.

Key features include:
- Recursive file renaming in a directory and its subdirectories
- Cross-platform compatibility (Windows, Mac, Linux)
- Handling of special characters in file names
- File conflict resolution with user prompts
- File size comparison for conflict resolution
- Option to keep both files by appending numbers to filenames

### Requirements

- Python 3.x
- Jupyter Notebook or JupyterLab

### Usage

To use the file renaming function:

1. Open the `file_rename.ipynb` notebook in Jupyter Notebook or JupyterLab.
2. Run all cells in the notebook to define the `rename_fn` function.
3. Use the `rename_fn` function in a new cell, providing the necessary parameters:

```python
rename_fn(folder_path, old_string, new_string)
```

- `folder_path`: The directory containing files to be renamed
- `old_string`: The current name or pattern to match
- `new_string`: The new name or pattern to replace with

Example usage:
```python
# For Mac/Linux:
rename_fn('/Volumes/', 'video - ', '')

# For Windows:
rename_fn(r'C:\Program Files\My Folder', 'old-', 'new-')
```

### Notes

- The notebook includes detailed comments and explanations for each part of the script.
- You can modify the script directly in the notebook if you need to customize its behavior.
- The script uses regular expressions for pattern matching, allowing for flexible search and replace operations.
- It includes error handling to manage potential issues during the renaming process.

### Caution

This utility can make significant changes to your file system. Always ensure you have backups of your data before running the script, especially when working with important files or large directories.

## 2. Git History Rewrite Script

**Filename**: `flexible_history_rewrite.sh`

### Description

The `flexible_history_rewrite.sh` script provides a way to interactively rebase and rewrite the entire Git history of a repository.

Key features include:
- Automatic detection of total commit count
- Interactive rebase from the root of the repository
- Force push to update remote repository
- Cleanup of refs and aggressive garbage collection

### Requirements

- Git
- Bash shell

### Installation

1. Ensure you have Git installed on your system.
2. Save the script as `flexible_history_rewrite.sh` in your repository.
3. Make the script executable: 
   ```
   chmod +x flexible_history_rewrite.sh
   ```

### Usage

The script should be used when you need to make significant changes to your repository's commit history, such as:
- Removing sensitive data from the entire Git history
- Restructuring the commit history for better clarity
- Combining or splitting commits
- Changing commit messages or author information throughout the history

To use the Git history rewrite script:

1. Navigate to your Git repository in the terminal.
2. Ensure you're on the main branch and it's up to date:
   ```
   git checkout main
   git pull origin main
   ```
3. Run the script:
   ```
   ./flexible_history_rewrite.sh
   ```

4. The script will initiate an interactive rebase. Your default text editor will open with a list of all commits in your repository.

5. Modify the commits as needed using commands like `reword`, `edit`, `squash`, `fixup`, or `drop`.

6. Save and close the file to start the rebase process.

7. Follow the prompts to complete the rebase process.

8. The script will automatically force push the changes to the remote repository once the rebase is complete.

### Notes

- The script includes error handling. If the initial rebase fails, it will attempt to rebase from the root of the repository.
- After the rebase, the script performs cleanup operations including ref expiration and garbage collection.

### Caution

This script rewrites Git history and force pushes the changes. Use with extreme caution, especially on shared repositories. It's recommended to create a backup branch before running this script:
```
git checkout -b backup_branch
git checkout main
```

Always communicate with your team before using this on a shared repository, as it can cause issues for other contributors.

## 3. File Processing and Code Consolidation Utility

**Filename**: `doc_consolidator.py`

### Description

This Python script provides versatile functions for file processing tasks, including file concatenation, directory structure generation, backup operations, and code consolidation.

Key features include:
- Recursive file processing in a directory and its subdirectories
- Support for multiple file extensions
- Exclusion of specified folders
- Safe file reading with multiple encoding attempts
- Code consolidation for analysis

### Requirements

- Python 3.x

### Installation

1. Save the script as `doc_consolidator.py` in your desired directory.
2. Ensure you have Python 3.x installed on your system.

### Usage

To use the utility functions, import them into your Python script or Jupyter notebook:

```python
from utility_scripts import process_files, consolidate_code
```

#### Code Consolidation

To consolidate code files of specific extensions into a single file:

```python
output_file = consolidate_code(
    root_path='/path/to/your/project',
    extensions=['.py', '.js', '.html'],
    output_filename='consolidated_code.txt',
    exclude_folders=['venv', 'node_modules']
)
print(f"Consolidated code saved to: {output_file}")
```

- `root_path`: The directory containing files to be consolidated
- `extensions`: List of file extensions to include (or a single extension as a string)
- `output_filename`: (Optional) Name of the output file
- `exclude_folders`: (Optional) List of folder names to exclude from processing

#### Other File Processing Tasks

For other file processing tasks like generating directory structure or creating backups, use the `process_files` function:

```python
# Generate directory structure
structure_file = process_files('structure', '/path/to/your/project', output_filename='project_structure.txt')

# Create backups
backup_log = process_files('backup', '/path/to/your/project', output_filename='backup_log.txt')
```

### Notes

- The script includes error handling and safe file reading to manage potential issues during processing.
- Consolidated output and logs are saved in the current working directory by default.

### Caution

This utility can process a large number of files and make changes to your file system. Always ensure you have backups of your data before running the script, especially when working with important files or large directories.

## 4. Newline Removal Utility

**Filename**: `remove_newlines.py`

### Description

This Python script provides a utility to remove unnecessary newlines from text files, consolidating paragraphs while preserving intentional line breaks between paragraphs.

### Requirements

- Python 3.x

### Usage

To use the newline removal utility:

```python
python remove_newlines.py <input_filename> [<output_filename>]
```

If no output filename is provided, the input file will be overwritten with the processed text.

### Notes

This script is useful for cleaning up text files with excessive line breaks, such as those copied from PDFs or web pages.
It preserves paragraph structure by maintaining double line breaks between paragraphs.
