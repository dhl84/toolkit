#!/bin/bash

set -e

# Ensure you're on the main branch and up to date
git checkout main
git pull origin main

# Count the number of commits
commit_count=$(git rev-list --count HEAD)

# Print the number of commits
echo "Your repository has $commit_count commits."

# Perform the interactive rebase
echo "Starting interactive rebase..."
if ! git rebase -i HEAD~$commit_count; then
    echo "Initial rebase failed. Attempting rebase from root..."
    if ! git rebase -i --root; then
        echo "Rebase failed. Aborting..."
        git rebase --abort
        exit 1
    fi
fi

# After the rebase is complete
echo "Rebase completed. Force pushing changes..."
git push origin main --force

# Clean up refs and garbage collect
git reflog expire --expire=now --all
git gc --prune=now --aggressive

echo "Process completed."