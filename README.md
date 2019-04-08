A sample django application that is configured to use https://github.com/mozilla/mozilla-django-oidc locally.

OIDC_RP_CLIENT_ID and OIDC_RP_CLIENT_SECRET must be configured in the .env before starting the application.

After running the development server, login by going to http://localhost:8000/hello/ and clicking 'Login'.

Alternatively, going to http://localhost:8000/hello/required/ will redirect you immediately to WebLogin.
