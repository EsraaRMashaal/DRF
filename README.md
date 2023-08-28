## get request in models DRF

#### Add in middleware folder this file 
```
request_exposer.py
```


#### Add in settings.py 

```
MIDDLEWARE = [
    'appName.middlewares.request_exposer.RequestExposerMiddleware'
]
```

#### To add signal : 


- Add  signals.py file to the app folder
- Add this in __init__.py
```
default_app_config = "appName.apps.appNameConfig"
```
-Add this in apps.py
```
from django.apps import AppConfig


class appNameConfig(AppConfig):
    name = 'appName'
    def ready(self):
        import appName.signals

```





