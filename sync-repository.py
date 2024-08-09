import os
import gitlab
import time

GITLAB_URL = os.environ.get('GITLAB_URL', None); assert GITLAB_URL is not None 
PRIVATE_TOKEN = os.environ.get('PRIVATE_TOKEN', None); assert PRIVATE_TOKEN is not None
PROJECT_ID = os.environ.get('PROJECT_ID', None); assert PROJECT_ID is not None
POLL_INTERVAL = os.environ.get('POLL_INTERVAL', 10)

# Initialize the GitLab connection
gl = gitlab.Gitlab(GITLAB_URL, private_token=PRIVATE_TOKEN)

# Get the project
project = gl.projects.get(PROJECT_ID)

# Trigger the pull mirror update
project.mirror_pull()

# Wait for the sync to complete
while True:
    mirror_pull_details = project.mirror_pull_details()
    mirror_status = mirror_pull_details['update_status']
    last_update_at = mirror_pull_details['last_update_at']
    last_update_started_at = mirror_pull_details['last_update_started_at']

    print(f"Mirror status: {mirror_status}")
    if mirror_status == 'finished':
        print("Pull mirror update completed successfully.")
        print(f"last_update_started_at: {last_update_started_at}")
        print(f"last_update_started_at: {last_update_started_at}")
        break
    elif mirror_status in ['failed', 'error']:
        print("Pull mirror update failed.")
        break
    time.sleep(POLL_INTERVAL)
