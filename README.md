
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


## TODO
- [x] a RESTful service. powered by DRF.
- [x] admin panel on [http://localhost:8000/accounts](http://localhost:8000/accounts)
- [ ] Default DB should be changed to MySQL or Postgres
- [ ] Admin user be able to change design of website.