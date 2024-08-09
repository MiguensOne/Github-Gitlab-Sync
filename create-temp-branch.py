from common import *

import gitlab

COMMIT_REF = os.getenv.get("COMMIT_REF", None); assert COMMIT_REF is not None, "COMMIT_REF environment variable is not set"

# Initialize GitLab connection
gl = gitlab.Gitlab(GITLAB_URL, private_token=PRIVATE_TOKEN)

# Get the project
project = gl.projects.get(PROJECT_ID)

# Define the new branch name
new_branch_name = f"pipeline-bridge/{COMMIT_REF}"

# Create the new branch
branch = project.branches.create({'branch': new_branch_name, 'ref': COMMIT_REF})

print(f"Branch '{new_branch_name}' created successfully.")