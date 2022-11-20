# SimpleLandingWebSite
I made this landing Web site while taking one of the online courses.  It has applications such as: Slider, CRM, CMS, Prices and Telegram bot that notifies about the application left on the site.
-------------------------------------------------------------------------------------------------------------------
# Second commit
Migrated from sqlite to PostgreSQL; Appropriate settings are set in settings.py (in the dictionary DATABASES);
psycopg2-binary library has been added to requirements.txt

# Third commit
Gunicorn has been added to requirements.txt; media and .env files has been added to .gitignore; Docker configs have been added for dev and prod versions; DEBUG, ALLOWED_HOSTS, DATABASES values are now hidden using environment variables (.env-files).

# Third commit (fix)
The static directory has been moved to the root of the project; Added STATICFILES_DIRS list to settings.py for correct work of collectstatic command

# Fourth commit
Added settings to Dockerfile.prod to be able to upload media files when the project is deployed on the server
