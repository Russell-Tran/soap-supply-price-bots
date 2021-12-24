# dispatch
* https://pancy.medium.com/running-a-https-python-server-on-ec2-in-5-minutes-6c1f0444a0cf
* https://caddyserver.com/docs/install#debian-ubuntu-raspbian

```
gunicorn --timeout 600 -w 1 -k uvicorn.workers.UvicornWorker main:app
```

and simultaneously,

```
caddy reverse-proxy --from [Public IPv4 DNS HERE has to be the EC2 domain not the raw ip] --to localhost:8000
```

## Notes
The Caddyfile from the tutorial did not work. Instead use:
```
caddy reverse-proxy --from [Public IPv4 DNS HERE] --to localhost:8000
```
From: https://caddyserver.com/docs/quick-starts/https

## Troubleshooting
* Both the Python "app" and Caddy need to be running simultaneously, of course
* Deal with caddy warnings. E.g. `caddy fmt --overwrite`

