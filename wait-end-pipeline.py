import os
from common import *
import time
import gitlab

PIPELINE_ID = os.environ.get("PIPELINE_ID", None)
assert PIPELINE_ID is not None, "PIPELINE_ID environment variable is not set"

gl = gitlab.Gitlab(GITLAB_URL, private_token=PRIVATE_TOKEN)
project = gl.projects.get(PROJECT_ID)

pipeline = project.pipelines.get(PIPELINE_ID)

while pipeline.status not in ["success", "failed", "canceled"]:
    pipeline.refresh()
    print(f"Pipeline status: {pipeline.status}")
    time.sleep(POLL_INTERVAL)

print(f"Pipeline finished with status: {pipeline.status}")
