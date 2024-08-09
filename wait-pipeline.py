import os
import common
import time

PIPELINE_ID = os.getenv.get("PIPELINE_ID", None); assert PIPELINE_ID is not None, "PIPELINE_ID environment variable is not set"

# Initialize GitLab connection
gl = gitlab.Gitlab(GITLAB_URL, private_token=PRIVATE_TOKEN)
project = gl.projects.get(PROJECT_ID)

pipeline = project.pipelines.get(PIPELINE_ID)

# Poll pipeline status
while pipeline.status not in ['success', 'failed', 'canceled']:
    pipeline.refresh()
    print(f"Pipeline status: {pipeline.status}")
    time.sleep(POLL_INTERVAL)

print(f"Pipeline finished with status: {pipeline.status}")

if pipeline.status != 'success':
    exit(1)