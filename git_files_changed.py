import sys
from lib.changed_files_finder import ChangedFilesFinder

if len(sys.argv) < 4:
    print("Usage: git_files_changed.py <repository-directory> <branch> <committer-email>")

else:
    changed_files_finder = ChangedFilesFinder(sys.argv[1], sys.argv[2], sys.argv[3])
    changed_files = changed_files_finder.find_changed_files()
    print("Changed files: " + str(len(changed_files)))
