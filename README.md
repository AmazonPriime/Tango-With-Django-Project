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
