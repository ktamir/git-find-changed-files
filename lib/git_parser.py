from lib.models.git_log_entry import GitLogEntry
from lib.models.git_object_type import GitObjectType

from lib.models.git_commit_object import GitCommitObject
from lib.models.git_tree_object import GitTreeObject


class GitParser:
    def parse_git_log(self, git_log_output):
        parsed_commits = []
        commits = git_log_output.decode('utf-8').split("commit ")
        for commit in commits[1:]:
            lines = commit.splitlines()
            commit_hash = lines[0]

            author_line = lines[1]
            author_name = author_line[8:author_line.find('<') - 1]
            author_email = author_line[author_line.find('<') + 1:author_line.find('>')]
            parsed_commits.append(GitLogEntry(commit_hash, author_name, author_email))
        return parsed_commits

    def parse_commit_object(self, commit_object_output):
        lines = commit_object_output.splitlines()
        tree_hash = lines[0][5:].decode('utf-8')
        parent_hash = lines[1][7:].decode('utf-8') if lines[1].startswith(b"parent") else None
        return GitCommitObject(tree_hash, parent_hash)

    def parse_tree_object(self, tree_object_output):
        parsed_tree_object = []
        for line in tree_object_output.splitlines():
            words = line.split()
            object_type = words[1].decode('utf-8')
            object_hash = words[2].decode('utf-8')
            object_name = words[3].decode('utf-8')
            if object_type == 'blob':
                object_type = GitObjectType.blob
            elif object_type == 'tree':
                object_type = GitObjectType.tree
            parsed_tree_object.append(GitTreeObject(object_type, object_hash, object_name))
        return parsed_tree_object
