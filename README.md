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
    
