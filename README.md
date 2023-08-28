## get request in models DRF

#### Add in middelware folder this file 
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


##### Add in the app folder this file 
```
signals.py
```

##### Add this in __init__.py
```
default_app_config = "appName.apps.appNameConfig"
```

##### Add this in apps.py
```
from django.apps import AppConfig


class appNameConfig(AppConfig):
    name = 'appName'
    def ready(self):
        import appName.signals

```





