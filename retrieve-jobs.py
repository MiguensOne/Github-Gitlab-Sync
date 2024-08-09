import common
import os

PIPELINE_ID = os.environ.get('PIPELINE_ID', None); assert PIPELINE_ID is not None, "PIPELINE_ID environment variable is not set"

# Initialize GitLab connection
gl = gitlab.Gitlab(GITLAB_URL, private_token=PRIVATE_TOKEN)

# Get the project
project = gl.projects.get(PROJECT_ID)

# Get the specific pipeline
pipeline = project.pipelines.get(PIPELINE_ID)

# Retrieve all jobs belonging to this pipeline
jobs = pipeline.jobs.list(all=True)

# Process jobs
for job in jobs:
    print(f"{job.id}:{job.name}")
    