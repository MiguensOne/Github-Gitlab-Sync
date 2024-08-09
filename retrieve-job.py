import common
import os
import time

JOB_ID = os.environ.get('JOB_ID', None); assert JOB_ID is not None, "JOB_ID environment variable is not set"

# Initialize GitLab connection
gl = gitlab.Gitlab(GITLAB_URL, private_token=PRIVATE_TOKEN)

# Get the project
project = gl.projects.get(PROJECT_ID)

# Get the job
job = project.jobs.get(JOB_ID)

# Wait until the job is done
while job.status not in ['success', 'failed', 'canceled']:
    time.sleep(POLL_INTERVAL)
    job.refresh()

# Retrieve and decode the log of the job
log_binary = job.trace()
log_decoded = log_binary.decode('utf-8')

# Pretty print the log
print(log_decoded)

if job.status != 'success':
    exit(1)

