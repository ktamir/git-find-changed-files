import sys

from lib.git_parser import GitParser
from lib.git_proxy import GitProxy
from lib.git_tree_comparer import GitTreeComparer


class ChangedFilesFinder:
    def __init__(self, repository_path, branch, committer_email):
        self.respository_path = repository_path
        self.branch = branch
        self.committer_email = committer_email

    def find_changed_files(self):
        proxy = GitProxy(self.branch, self.respository_path)
        parser = GitParser()
        tree_comparer = GitTreeComparer(proxy, parser)
        committer_email = sys.argv[3]

        changed_files = set()

        parsed_git_log = parser.parse_git_log(proxy.get_branch_log())
        commits_by_user = [commit for commit in parsed_git_log if commit.author_email == committer_email]
        for commit in commits_by_user:
            commit_object = parser.parse_commit_object(proxy.get_git_object(commit.commit_hash))
            current_commit_tree = parser.parse_tree_object(proxy.get_git_object(commit_object.tree_hash))

            if commit_object.parent_hash is not None:
                parent_commit_object = parser.parse_commit_object(proxy.get_git_object(commit_object.parent_hash))
                parent_commit_tree = parser.parse_tree_object(proxy.get_git_object(parent_commit_object.tree_hash))
            else:
                parent_commit_tree = []

            tree_comparer.get_tree_diff(parent_commit_tree, current_commit_tree, '/', changed_files)
        return changed_files