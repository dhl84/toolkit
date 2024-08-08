```markdown
# Cross-Platform File Renaming Utility

## Description

This Python utility provides a robust, cross-platform function for renaming files within a specified directory and its subdirectories. It's designed to work seamlessly on both Windows and Unix-based systems (Mac/Linux).

Key features include:
- Recursive file renaming in a directory and its subdirectories
- Cross-platform compatibility (Windows, Mac, Linux)
- Handling of special characters in file names
- File conflict resolution with user prompts
- File size comparison for conflict resolution
- Option to keep both files by appending numbers to filenames

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Save the script as `rename_utility.py` in your desired directory.

## Usage

To use the file renaming function, follow these steps:

1. Import the function in your Python script or interactive session:

   ```python
   from rename_utility import rename_fn
   ```

2. Call the function with appropriate parameters:

   ```python
   rename_fn(folder_path, old_string, new_string)
   ```

   - `folder_path`: The path to the directory where you want to start the renaming process.
   - `old_string`: The string in the filename you want to replace.
   - `new_string`: The string you want to replace it with (can be an empty string).

### Examples

For Mac/Linux:
```python
rename_fn('/Volumes/downloads/MyFolder', 'old-', 'new-')
```

For Windows:
```python
rename_fn(r'C:\Users\YourName\Documents\MyFolder', 'old-', 'new-')
```

## Features

### Cross-Platform Compatibility
The function automatically handles path differences between Windows and Unix-based systems.

### Special Character Handling
Special characters in filenames are properly escaped and handled.

### Conflict Resolution
If a file with the new name already exists, the function will:
1. Compare file sizes
2. Prompt the user with options:
   - Overwrite the existing file
   - Keep both files (auto-incrementing number added to the new filename)
   - Skip renaming this file

## Notes

- Always ensure you have backups of important files before performing bulk renaming operations.
- The function will recursively search all subdirectories of the specified folder path.
- File renaming is performed in-place and cannot be undone automatically.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page] if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)
```
