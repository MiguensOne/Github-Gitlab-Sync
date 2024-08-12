import os
from common import *
import time
import gitlab
import sys


COMMIT_REF = os.environ.get("COMMIT_REF", None)
assert COMMIT_REF is not None, "COMMIT_REF environment variable is not set"

gl = gitlab.Gitlab(GITLAB_URL, private_token=PRIVATE_TOKEN)

project = gl.projects.get(PROJECT_ID)

pipeline = project.pipelines.create({"ref": f"pipeline-bridge/{COMMIT_REF}"})
print(f"{pipeline.id}")
print(f"GITLAB PIPELINE LINK {pipeline.web_url}", file=sys.stderr)
time.sleep(POLL_INTERVAL)
