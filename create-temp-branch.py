from common import *

import gitlab

COMMIT_REF = os.environ.get("COMMIT_REF", None)
assert COMMIT_REF is not None, "COMMIT_REF environment variable is not set"

gl = gitlab.Gitlab(GITLAB_URL, private_token=PRIVATE_TOKEN)

project = gl.projects.get(PROJECT_ID)

new_branch_name = f"pipeline-bridge/{COMMIT_REF}"

try:
    branch = project.branches.create({"branch": new_branch_name, "ref": COMMIT_REF})
    print(f"Branch '{new_branch_name}' created successfully.")
except Exception as e:
    print(f"Failed to create branch {new_branch_name}. Reason: {str(e)}")
