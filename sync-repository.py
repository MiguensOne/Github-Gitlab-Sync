import gitlab
import time

from common import *

gl = gitlab.Gitlab(GITLAB_URL, private_token=PRIVATE_TOKEN)

project = gl.projects.get(PROJECT_ID)

project.mirror_pull()
time.sleep(POLL_INTERVAL)

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
