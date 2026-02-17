from common import *
import os
import json
import gitlab

PIPELINE_ID = os.environ.get("PIPELINE_ID", None)
assert PIPELINE_ID is not None, "PIPELINE_ID environment variable is not set"

gl = gitlab.Gitlab(GITLAB_URL, private_token=PRIVATE_TOKEN)

project = gl.projects.get(PROJECT_ID)

pipeline = project.pipelines.get(PIPELINE_ID)

jobs = pipeline.jobs.list(all=True)

jobs_list = []

counter = 1

for i in jobs:
    job_id = str(i.id)
    job_name = str(i.name)
    key = counter
    counter += 1
    jobs_list.append(
        {
            "name": job_name,
            "JOB_ID": job_id,
            "key": key,
        }
    )

print(json.dumps(jobs_list, separators=(",", ":")))
