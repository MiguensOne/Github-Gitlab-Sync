import os
import urllib.parse

GITLAB_URL = os.environ.get("GITLAB_URL", None)
assert GITLAB_URL is not None
PRIVATE_TOKEN = os.environ.get("GITLAB_TOKEN", None)
assert PRIVATE_TOKEN is not None
PROJECT_ID = os.environ.get("PROJECT_ID", None)
assert PROJECT_ID is not None
POLL_INTERVAL = os.environ.get("POLL_INTERVAL", 10)


def sanitize_ref_for_branch_name(ref):
    """
    Sanitize a git ref to create a valid GitLab branch name.
    
    GitLab branch names cannot contain certain characters like spaces or square brackets.
    This function replaces problematic characters to ensure branch names are valid.
    
    Args:
        ref: The git reference (commit SHA, branch name, etc.)
        
    Returns:
        A sanitized string safe to use in GitLab branch names
    """
    # Replace spaces with hyphens
    sanitized = ref.replace(' ', '-')
    # Replace square brackets with parentheses
    sanitized = sanitized.replace('[', '(').replace(']', ')')
    return sanitized
