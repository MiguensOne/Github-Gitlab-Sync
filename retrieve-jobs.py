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

for i in jobs:
    id = str(i.id)
    # Sanitize job name: replace spaces with underscores, remove brackets and other special chars
    name = re.sub(r'[^\w\s-]', '', str(i.name))  # Remove special chars except word chars, spaces, hyphens
    name = name.replace(" ", "_")  # Replace spaces with underscores
    jobs_list.append(str(f"{name} #{id}"))

print(json.dumps(jobs_list))
