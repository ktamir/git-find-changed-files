class GitCommitObject:
    def __init__(self, tree_hash, parent_hash=None):
        self.tree_hash = tree_hash
        self.parent_hash = parent_hash