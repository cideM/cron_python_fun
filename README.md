## Getting started

```shell
$ docker build -t foo .
$ docker run -t foo:latest
INFO[2023-08-30T16:46:26Z] read crontab: crontab
INFO[2023-08-30T16:46:30Z] starting                                      iteration=0 job.command="timeout 2 python ./job.py" job.position=0 job.schedule="*/5 * * * * * *"
INFO[2023-08-30T16:46:30Z] Hello world!                                  channel=stdout iteration=0 job.command="timeout 2 python ./job.py" job.position=0 job.schedule="*/5 * * * * * *"
INFO[2023-08-30T16:46:32Z] Cleaning up                                   channel=stdout iteration=0 job.command="timeout 2 python ./job.py" job.position=0 job.schedule="*/5 * * * * * *"
INFO[2023-08-30T16:46:32Z] Exit                                          channel=stdout iteration=0 job.command="timeout 2 python ./job.py" job.position=0 job.schedule="*/5 * * * * * *"
INFO[2023-08-30T16:46:32Z] job succeeded                                 iteration=0 job.command="timeout 2 python ./job.py" job.position=0 job.schedule="*/5 * * * * * *"
^C
INFO[2023-08-30T16:46:32Z] received interrupt, shutting down
INFO[2023-08-30T16:46:32Z] waiting for jobs to finish
INFO[2023-08-30T16:46:32Z] exiting
```

## Development

- To change how long the Python process runs, adjust `job.py`
- To change how long the Python process is allowed to run, change the `timeout 2` in `./crontab`
- To change the schedule, change the crontab values in `./crontab`; since this is using [supercronic](https://github.com/aptible/supercronic) you have a few more scheduling options such as seconds (which cron doesn't support)
