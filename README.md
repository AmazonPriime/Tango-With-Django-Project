## Django with Tango 2

Working for the WAD2 course labs at the University of Glasgow based on the ebook [Tango with Django](https://www.tangowithdjango.com/)

#### Takeaways from the book:
* Task 3
  * Creating a Django project
    * ```python3 manage.py startproject <project name>```
  * Creating a Django app
    * ```python3 manage.py createapp <app name>```
    * add app to Django project ```INSTALLED_APPS``` in ```settings.py```
    * add mapping in project ```urls.py``` ```path('<app name>/', include('<app name>.urls'))```
    * create a ```urls.py``` in your app folder

* Task 4
  * Using templates
    * create a ```templates``` directory in the main project folder
    * within that directory put another directory for any apps being used
    * in the apps ```views.py``` return render function
      * ```return render(request, '<template name>', context = context_dict)```
      * ```context_dict``` stores values to go into ```{{ template tags }}```
    * ensure the view is mapped in the ```urls.py```
  * Static files
    * create ```static``` directory in the project directory
    * add path to the static directory in the ```STATICFILES_DIRS```
    * in templates using static files put ```{% load staticfiles %}``` between ```<head>``` and ```<!DOCTYPE html>```

* Task 5
  * Database setup
    * configure which data will be used in the ```DATABASE``` section of the ```settings.py```
  * Models
    * create the model in the app/project ```models.py```, ```class <model name>(models.Model)```
    * register the model inside of the ```admin.py```, the one where the model from ```admin.site.register(<model name>)```
    * run the command ```python3 manage.py makemigrations <app name>``` and apply it with ```python3 manage.py migrate```
    * recommended: create a population script for testing
  * Deleting DB
    * delete the database file, usually: ```db.sqlite3```
    * delete the migrations from the migrations folder in app or project
    * run the migration commands ```python3 manage.py makemigrations <app name>``` and ```python3 manage.py migrate```
    * create a superuser account ```python3 manage.py createsuperuser```

* Task 6
  * Slugs
    * import the slug filter via ```from django.template.defaultfilters import slugify```
    * utilise the slug field via ```slug = models.SlugField()```
    * override the default save method for the model
      * ```python3
		def save(self, *args, **kwargs):
        	self.slug = slugify(self.name)
        	super(Category, self).save(*args, **kwargs)
        ```
  * Parameter passing in urls
    * add them as parameters in the view in ```views.py``` after the request parameter
    * add them into the ```urls.py``` ```path('category/<<type>:<paremeter name>>/', views.<view name>, name = '<view name>'),```
  * Loops and conditionals in templates
    * fixed loops: ```{% for n in numbers %} <h1>{{ n }}</h1> {% endfor %}```
    * conditionals: ```{% if n == 1 %} <h1>The number is 1</h1> {% else %} <h1>The number is not 1</h1> {% endif %}```

* Task 7
  * Forms
    * create a ```forms.py``` in the app or project - depending on which one needs it
    * create a form class for each form ```class <form name>(forms.ModelForm)```
    * inside nested ```class Meta``` associate the form with a model ```model = <model name>```
    * within the Meta class you can also include or exclude specific fields ```fields = (<fields>)``` ```exclude = (<fields>)```
  * Form template
    * uses ```<form id="<id describing form>" method="post" action="<url which in the url mappings points to form view>"></form>``` HTML tags
    * requires that you use the tag ```{% csrf_token %}```
    * hidden fields must be added in template: ```{% for hidden in form.hidden_fields %} {{ hidden }} {% endfor %}```
    * user fields must be added in template: ```{% for field in form.visible_fields %} {{ field.errors }} {{ field.help_text }} {{ field }} {% endfor %}```
