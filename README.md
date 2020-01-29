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
    
