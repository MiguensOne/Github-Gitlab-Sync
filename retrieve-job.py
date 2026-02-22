from common import *
import os
import time
import gitlab

JOB_ID = os.environ.get("JOB_ID", None)
assert JOB_ID is not None, "JOB_ID environment variable is not set"

gl = gitlab.Gitlab(GITLAB_URL, private_token=PRIVATE_TOKEN)

project = gl.projects.get(PROJECT_ID)

job = project.jobs.get(JOB_ID)

url = job.web_url
border = "#" * (len(url) + 4)
print(border)
print(f"# {url} #")
print(border)

lines_printed = 0


def print_new_lines(log_binary):
    global lines_printed
    lines = log_binary.decode("utf-8").splitlines()
    if len(lines) < lines_printed:
        lines_printed = 0
    for line in lines[lines_printed:]:
        print(line, flush=True)
    lines_printed = len(lines)


while job.status not in ["success", "failed", "canceled", "skipped", "manual"]:
    try:
        print_new_lines(job.trace())
    except Exception:
        pass
    time.sleep(POLL_INTERVAL)
    job.refresh()

if job.status == "manual":
    print("Job is in manual state. Please trigger it manually:")
    print(job.web_url)
    exit(0)

print_new_lines(job.trace())

print(f"GITLAB JOB STATUS: {job.status}")

if job.status != "success" and job.status != "manual":
    exit(1)
