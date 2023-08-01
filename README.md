# pythonDjangoProject


'''
1. This is based on swagger view because its little bit easy and we can provide authentication. Using Tokens.
2. If we want to run app then command is python manage.py runserver then results will found in http://localhost:8000/api/docs because we mentioned localhost in the ALLOWED_HOST and CORS_ALLOWED_ORIGINS in the settings.py file.
3. Then i created the app name as djangoAssignment and we should mention the new apps were created in the project settings INSTALLED_APPS and the connection was setup with postgresql in the settings .
4. Then I created the model as Place and serializer for that api and then i started doing functionality in the view using APIView
that will supports the CRUD operations. 
5. Then i created urls in the app and setup url path in project and metioned view as swagger view from drf_spectacular.
''''