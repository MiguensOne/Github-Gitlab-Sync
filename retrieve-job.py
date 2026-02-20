from common import *
import os
import time
import gitlab

JOB_ID = os.environ.get("JOB_ID", None)
assert JOB_ID is not None, "JOB_ID environment variable is not set"

gl = gitlab.Gitlab(GITLAB_URL, private_token=PRIVATE_TOKEN)

project = gl.projects.get(PROJECT_ID)

job = project.jobs.get(JOB_ID)

while job.status not in ["success", "failed", "canceled", "skipped", "manual"]:
    time.sleep(POLL_INTERVAL)
    job.refresh()

if job.status == "manual":
    print("Job is in manual state. Please trigger it manually:")
    print(job.web_url)
    exit(0)

log_binary = job.trace()
log_decoded = log_binary.decode("utf-8")

print(log_decoded)

print(f"GITLAB JOB STATUS: {job.status}")

if job.status != "success" and job.status != "manual":
    exit(1)
