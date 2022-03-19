## JobSche

A Flask web server for job scheduling. Everything is on the application server and
only the scheduling part would be handled by this web server. This is not suitable
for long running jobs.

### Job Types
 - RegularJob (Job that would run immediately)
 - DelayedJob (Job that would be executed after a specific time elapses)
 - ScheduledJob (Job that would be executed at a specific time)
 - RecurrentJob (Job that would be executed at a specific interval)

 ### What the application server needs
- Call the specific scheduling endpoint with (
    retries,
    backoff,
    webhook that executes the task that the job requires,
    webhook that would handle the result
)
