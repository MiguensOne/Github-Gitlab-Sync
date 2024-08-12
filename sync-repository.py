import gitlab
import time
import os

from common import *

COMMIT_REF = os.environ.get("COMMIT_REF", None)
assert COMMIT_REF is not None, "COMMIT_REF environment variable is not set"

gl = gitlab.Gitlab(GITLAB_URL, private_token=PRIVATE_TOKEN)
project = gl.projects.get(PROJECT_ID)

project.mirror_pull()
time.sleep(POLL_INTERVAL)

def is_commit_present(project, commit_ref):
    try:
        commit = project.commits.get(commit_ref)
        return True if commit else False
    except gitlab.exceptions.GitlabGetError:
        return False

# Poll the repository to check if the commit is present
while True:
    if is_commit_present(project, COMMIT_REF):
        print(f"Commit {COMMIT_REF} is present in the repository.")
        break
    time.sleep(POLL_INTERVAL)