import os
import subprocess


class GitProxy:
    def __init__(self, branch_name, repository_path):
        self.branch_name = branch_name
        self.repository_path = repository_path

    def get_branch_log(self):
        os.chdir(self.repository_path)
        process = subprocess.Popen(["git", "log", self.branch_name], stdout=subprocess.PIPE)
        output, err = process.communicate()
        return output

    def get_git_object(self, object_hash):
        os.chdir(self.repository_path)
        process = subprocess.Popen(["git", "cat-file", "-p", object_hash], stdout=subprocess.PIPE)
        output, err = process.communicate()
        return output
