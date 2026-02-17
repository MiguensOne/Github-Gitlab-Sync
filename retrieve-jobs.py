from common import *
import os
import json
import re
import gitlab

PIPELINE_ID = os.environ.get("PIPELINE_ID", None)
assert PIPELINE_ID is not None, "PIPELINE_ID environment variable is not set"

gl = gitlab.Gitlab(GITLAB_URL, private_token=PRIVATE_TOKEN)

project = gl.projects.get(PROJECT_ID)

pipeline = project.pipelines.get(PIPELINE_ID)

jobs = pipeline.jobs.list(all=True)

jobs_list = []

def build_github_key(job_name: str, job_id: str) -> str:
    raw_key = f"{job_name}_{job_id}"
    key = re.sub(r"[^\w-]", "_", raw_key)
    key = re.sub(r"_+", "_", key)
    key = key.strip("_-")
    if not key:
        key = f"job_{job_id}"
    return key


for i in jobs:
    job_id = str(i.id)
    job_name = str(i.name)
    key = build_github_key(job_name, job_id)
    jobs_list.append(
        {
            "name": job_name,
            "JOB_ID": job_id,
            "key": key,
        }
    )

print(json.dumps(jobs_list, separators=(",", ":")))
