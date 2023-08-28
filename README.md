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




