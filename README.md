# Github-Gitlab-Sync

This project enables you to run Gitlab Pipelines from Github Actions, allowing you to map all jobs from Gitlab into Github Actions and fetch the logs seamlessly.

## Features

- **Integration**: Leverage Gitlab's CI/CD capabilities within Github Actions workflows.
- **Job Mapping**: Automatically map Gitlab jobs to Github Actions.
- **Log Fetching**: Retrieve and display logs from Gitlab jobs in Github Actions.

## Known Limitations

- A job with `allow-failure` in Gitlab will show as failed in Github Actions. Therefore, the Github Action will appear with an "X" instead of an exclamation mark "!" as in Gitlab CI/CD.

## Recommendations

### How to Use

1. **Download the Workflow File**: Download the file `gitlab-bridge.yml` and place it in your `.github/workflows` directory in your Github repository.
2. **Set Up Environment Variables**: Configure the necessary environment variables in your Github Actions workflow file. These variables include your Gitlab API token, project ID, and other relevant details.
3. **Configure the Workflow**: Customize the workflow to run the Gitlab Pipelines using the provided scripts or according to your needs.
4. **Commit and Push**: Commit and push your changes to your Github repository.

### Gitlab CI/CD

- **Job Naming**: Keep the names of the jobs with normal characters. Spaces will be mapped with underscores.
- **Avoid Double Triggering**: Use a top-level condition `CI_PIPELINE_SOURCE == "api"` to avoid double triggering (via API and branch creation).

## Requirements

- **Accounts**: Git, Github, and Gitlab accounts.
- **Knowledge**: Basic understanding of CI/CD concepts and YAML syntax.

## Installation

No additional installation is needed, as the project relies on Github Actions and Gitlab CI/CD out-of-the-box.

## Project Structure

- `README.md`: Project documentation.
- `common.py`: Shared functions or classes used across multiple scripts.
- `create-temp-branch.py`: Script to create a temporary branch.
- `retrieve-job.py`: Script to retrieve a specific job.
- `retrieve-jobs.py`: Script to retrieve multiple jobs.
- `sync-repository.py`: Script to synchronize the repository.
- `trigger-pipeline.py`: Script to trigger a pipeline.
- `wait-pipeline.py`: Script to wait for a pipeline to complete.

## License

This project is licensed under the APACHE-2.0 License and provide AS-IS.
