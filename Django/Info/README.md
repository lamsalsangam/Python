### PROCEDURE

## Install the django in the system

## Create the project like this:

```
django-admin startproject Info
```

# `Info` is the folder name

# To run the program do this:

```
py manage.py runserver
```

# Create the new app or the route that you want in your app like this:

```
py manage.py startapp [APPNAME]
```

## for routing purpose create the `urls.py` in the `[APPANME]` make it easier

# now specify the `path` in the `Info` folder urls.py

# Make the `views.py` in the `[APPNAME]` as you wish . It is for the user view purpose

### Create the `templates` folder in the [APPNAME] and inside it you can provide the route path example and create the `html` templates

## For the `stylesheet` Create the `static` folder inside the `[APPNAME]` and provide the route to the `.css` file.

# to load the css file in the `.html` page write `{%load static%}` and reference the link like

```
<link rel="stylesheet" href="{%static 'newyear/styles.css'%}" />
```

## Use the django provided templating language sequence like `{{}}` and `{% coditions/loop %}` --->`{% endconditions/loop %}`

### We can create the `layout.html` for the the html and only change the part that will differ in the one app by doing this to follow the `DRY` Principle

# Add `{% block body %} {% endblock %}` in the `layout.html` and in the `.html` file that should be present inside the the `block` just extend it by `{% extends "[APPNAME/FILENAME]/layout.html" %}`

# Then wrap the content to be presented inside `{% block body %} {% endblock %}` in the routed file.

## This idea is called the template inheritance

# You have `python manage.py migrate` to enable or connect with the inbuilt database of django
