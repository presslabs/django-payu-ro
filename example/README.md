# Running the example application

Assuming you use virtualenv, follow these steps to download and run the
django-payu example application in this directory:

```
$ git clone git://github.com/PressLabs/django-payu.git
$ cd django-payu/example
$ virtualenv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```

Now we need to create the database tables and an admin user.
On Django 1.6 and below, run the following and when prompted to create a
superuser choose yes and follow the instructions:

```
$ python manage.py syncdb --migrate
```

On Django 1.7 and above:

```
$ python manage.py migrate
$ python manage.py createsuperuser
```

Now you need to run the Django development server:

```
$ python manage.py runserver
```

You should then be able to open your browser on http://127.0.0.1:8000 and see
a page with a payu form.
