from common import *

import gitlab

COMMIT_REF = os.environ.get("COMMIT_REF", None); assert COMMIT_REF is not None, "COMMIT_REF environment variable is not set"

gl = gitlab.Gitlab(GITLAB_URL, private_token=PRIVATE_TOKEN)

project = gl.projects.get(PROJECT_ID)

branch_name_to_delete = f"pipeline-bridge/{COMMIT_REF}"

try:
    project.branches.delete(branch_name_to_delete)
    print(f"Branch '{branch_name_to_delete}' deleted successfully.")
except Exception as e:
    print(f"Failed to delete branch {branch_name_to_delete}. Reason: {str(e)}")
