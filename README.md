# sso-examples-oidc-sp-mozillaoidc-sample
A sample django application that is configured to use https://github.com/mozilla/mozilla-django-oidc locally.

# Prerequisites
docker and docker-compose installed locally
- https://docs.docker.com/get-docker/
- https://docs.docker.com/compose/install/

# Setup
git clone this repository and change to the directory

For local development rename `src/dev.sample.env` to `src/.env` 

OIDC_RP_CLIENT_ID and OIDC_RP_CLIENT_SECRET must be configured in `.env` before starting the application.

# Starting the app

```
docker-compose up
```

After starting the development server, login by going to http://localhost:8000/hello/ and clicking 'Login'.

Alternatively, going to http://localhost:8000/hello/required/ will redirect you immediately to WebLogin.
