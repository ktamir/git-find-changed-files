class GitLogEntry:
    def __init__(self, commit_hash, author_name, author_email):
        self.commit_hash = commit_hash
        self.author_name = author_name
        self.author_email = author_email