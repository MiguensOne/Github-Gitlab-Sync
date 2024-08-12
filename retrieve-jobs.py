from common import *
import os
import gitlab

PIPELINE_ID = os.environ.get('PIPELINE_ID', None); assert PIPELINE_ID is not None, "PIPELINE_ID environment variable is not set"

gl = gitlab.Gitlab(GITLAB_URL, private_token=PRIVATE_TOKEN)

project = gl.projects.get(PROJECT_ID)

pipeline = project.pipelines.get(PIPELINE_ID)

jobs = pipeline.jobs.list(all=True)

jobs_list = []

for i in jobs:
    id = str(i.id)
    name = str(i.name).replace(' ', '_')
    jobs_list.append(str(f"{name} #{id}"))

print(','.join(jobs_list))
