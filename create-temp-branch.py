import gitlab

# Configuration
GITLAB_URL = "https://gitlab.com"
PRIVATE_TOKEN = "your_private_token"
PROJECT_ID = "your_project_id"
COMMIT_REF = "your_commit_ref"  # The commit hash to base the new branch on

# Initialize GitLab connection
gl = gitlab.Gitlab(GITLAB_URL, private_token=PRIVATE_TOKEN)

# Get the project
project = gl.projects.get(PROJECT_ID)

# Define the new branch name
new_branch_name = f"pipeline-bridge/{COMMIT_REF}"

# Create the new branch
branch = project.branches.create({'branch': new_branch_name, 'ref': COMMIT_REF})

print(f"Branch '{new_branch_name}' created successfully.")