from lib.models.git_object_type import GitObjectType


class GitTreeComparer:
    def __init__(self, git_proxy, git_parser):
        self.git_proxy = git_proxy
        self.git_parser = git_parser

    def get_tree_diff(self, first_tree, second_tree, working_directory, diff):
        first_tree_file_names = {working_directory + tree_object.name for tree_object in first_tree}
        second_tree_file_names = {working_directory + tree_object.name for tree_object in second_tree}
        # Find symmetric differences between the tree file name sets - finds files created or deleted
        diff.update(first_tree_file_names.symmetric_difference(second_tree_file_names))

        for first_tree_item in first_tree:
            for second_tree_item in second_tree:
                if first_tree_item.type == GitObjectType.blob:
                    if first_tree_item.name == second_tree_item.name:
                        if first_tree_item.hash != second_tree_item.hash:
                            # File changed
                            diff.add(working_directory + first_tree_item.name)
                elif first_tree_item.name == second_tree_item.name:
                    # Found a tree present in both commits, find the diffs between the trees
                    new_first_tree = self.git_parser.parse_tree_object(
                        self.git_proxy.get_git_object(second_tree_item.hash))
                    new_second_tree = self.git_parser.parse_tree_object(
                        self.git_proxy.get_git_object(first_tree_item.hash))

                    self.get_tree_diff(new_first_tree, new_second_tree, working_directory
                                       + first_tree_item.name + "/", diff)
