import datetime

with open('daily_job.log', 'a') as f:
    now = datetime.datetime.now()
    f.write(f"Job ran at: {now.isoformat()}\n")

print(f"Daily job ran at {now}") 