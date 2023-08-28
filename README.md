## get request in models DRF

#### 1. Add request_exposer.py file in middleware folder


#### 2. Add in settings.py 

```
MIDDLEWARE = [
    'appName.middlewares.request_exposer.RequestExposerMiddleware'
]
```

#### 3. To add signals : 


- Add  signals.py file to the app folder
- Add this in __init__.py
```
default_app_config = "appName.apps.appNameConfig"
```
- Add this in apps.py
```
from django.apps import AppConfig


class appNameConfig(AppConfig):
    name = 'appName'
    def ready(self):
        import appName.signals

```





