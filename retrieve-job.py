from common import *
import os
import time
import gitlab

JOB_ID = os.environ.get('JOB_ID', None); assert JOB_ID is not None, "JOB_ID environment variable is not set"

gl = gitlab.Gitlab(GITLAB_URL, private_token=PRIVATE_TOKEN)

project = gl.projects.get(PROJECT_ID)

job = project.jobs.get(JOB_ID)

while job.status not in ['success', 'failed', 'canceled', 'skipped']:
    time.sleep(POLL_INTERVAL)
    job.refresh()

log_binary = job.trace()
log_decoded = log_binary.decode('utf-8')

print(log_decoded)

print(f"GITLAB JOB STATUS: {job.status}")

if job.status != 'success':
    exit(1)

