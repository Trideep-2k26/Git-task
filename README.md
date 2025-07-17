# GitHub Action: Daily Python Job

This repository includes a GitHub Actions workflow that runs a Python script (`daily_job.py`) every day at midnight UTC.

## Files
- `.github/workflows/daily_python_job.yml`: The workflow definition.
- `daily_job.py`: The Python script that will be executed daily.

## How It Works
- The workflow is triggered daily by a cron schedule (`0 0 * * *`).
- It checks out the repository, sets up Python, installs dependencies (if `requirements.txt` exists), and runs `daily_job.py`.
- The script appends the current date and time to `daily_job.log` and prints a message.

## How to Test Locally
1. Make sure you have Python 3 installed.
2. Run the script manually:
   ```bash
   python daily_job.py
   ```
3. Check the `daily_job.log` file to see the log entry.

## How to Test the GitHub Action
1. Push your changes to GitHub.
2. Go to the "Actions" tab in your repository.
3. You can manually trigger the workflow by clicking "Run workflow" (thanks to `workflow_dispatch`).
4. After the workflow runs, check the logs in the GitHub Actions UI to see the output.

## Customization
- To change the schedule, edit the `cron` value in `.github/workflows/daily_python_job.yml`.
- To run a different script, change the script name in the workflow and update your Python file accordingly. 
