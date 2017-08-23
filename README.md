# XRP MONITOR

## Setup

Install requirements:

`pip install -r requirements/requirements.txt`

```
export API_KEY='your api key'
```

Configure a cron

`crontab -e`

Add the following line:

`*/5 * * * * source [file with api_key] && python [path-to-project/application.py]`

Install the Datadog Agent and configure it to send custom metrics

Configure a Datadog Monitor with the alert price
