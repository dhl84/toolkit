# __init__.py for toolkit project

# Import the remove_newlines function
from .remove_newlines import remove_newlines

# We can't directly import from the Jupyter notebook,
# so we'll add a note about its usage
file_rename_note = """
The file renaming utility is available in the 'file_rename.ipynb' Jupyter notebook.
To use it, open the notebook and run all cells to define the 'rename_fn' function.
Then you can use it as follows:
    rename_fn(folder_path, old_string, new_string)
"""

# Add a note about the bash script
flexible_history_rewrite_note = """
The 'flexible_history_rewrite.sh' script is a bash script for Git history rewriting.
It should be run from the command line, not imported as a Python module.
"""

# Define what should be imported when using "from toolkit import *"
__all__ = ['remove_newlines']

# You could also add version information
__version__ = '0.1.0'

print("Toolkit initialized. Available functions: remove_newlines")
print(file_rename_note)
print(flexible_history_rewrite_note)