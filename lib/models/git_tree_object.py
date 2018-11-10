class GitTreeObject:
    # A git tree object, received from running git cat-file -p {tree_hash}
    # For example: 100644 blob cf59e02c3d2a2413e2da9e535d3c116af1077906    README.md
    def __init__(self, type, hash, name):
        self.type = type
        self.hash = hash
        self.name = name