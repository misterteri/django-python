## Creating a new project

1. create a new skeleton project
   ```bash
   django-admin startproject project-name
   ```
2. create a new app
   ```bash
   python manage.py startapp app-name
   ```
3. add the app to the project
   ```python
   # project-name/settings.py
   INSTALLED_APPS = [
       'app-name.apps.AppNameConfig',
       ...
   ]
   ```

## Running the server

```bash
python manage.py runserver
```

## Adding a new page to the app

1.add urls in project-name/urls.py

2. add urls in app-name/urls.py

3. define 'view' in app-name/views.py

4. add templates in project-name/app-name/templates/..
