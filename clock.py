from datetime import datetime
from mainClass import love
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()
# Schedule job_function to be called every two hours
sched.add_job(love, 'interval', seconds=2)

sched.start()