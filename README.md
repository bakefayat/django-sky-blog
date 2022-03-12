
# Django Simple Blog

A simple Content Management system powered by Django.

## How to run in linux

To run this project in development mode; Just use steps below:

1. Install `python3`, `pip`, `virtualenv` in your system.
2. Clone the project `https://github.com/bakefayat/django-simple-blog`.
3. Make development environment ready using commands below;

  ```bash
  git clone https://github.com/bakefayat/django-simple-blog && cd django-simple-blog
  python3 -m venv .venv  # Create virtualenv named .venv in linux (windows is different.)
  source .venv/bin/activate
  pip install -r requirements.txt
  mv  .env-sample .env
  nano .env ()
  python manage.py migrate  # Create database tables
  python manage.py createsuperuser # Create superuser.
  ```

4. Run project using `python manage.py runserver`
5. Go to [http://localhost:8000](http://localhost:8000) to see your simple blog.

## Production mode
before running this project on the production make sure to do these steps:
1. change default SQLite database to Postgresql or MySQL.
2. change DEBUG=True to DEBUG=False (you can also create additional settings.py file for production.)
3. uninstall django debug toolbar.

##Run project in replit.com
replit is a online code editor. it also gives you hosting of your project.<br>
follow steps bellow:
1. clone github project on replit.
2. install requirements file with pip.
3. follow secrets guide on replit for SECRET_KEY of project.
4. set ALLOWED_HOSTS in settings file to ```['*']```
5. run migrate command on console: ```python manage.py migrate```
6. add below line to settings file to fix CSRF_TOKEN error.
```
CSRF_TRUSTED_ORIGINS = [your replit url like: 'https://django-simple-blog.ehsanbakefayat.repl.co']
```
6. add these lines to .replit file
```
language = "python3"
run = "python manage.py runserver 0.0.0.0:8000"
```
7. set DEBUG = FALSE in settings.py
8. remove debug_toolbar from INSTALLED_APPS and middlewares.
9. hit run button and enjoy it!

## TODO
- [x] a RESTful service. powered by DRF.
- [x] Comment system.
- [x] admin panel on [http://localhost:8000/accounts](http://localhost:8000/accounts)
- [ ] Modular frontend.
- [ ] Default DB should be changed to MySQL or Postgres.
- [ ] Admin user be able to change design of website.