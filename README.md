## get request in models DRF

#### Add in settings.py 

```
MIDDLEWARE = [
    'remotePlatz.middlewares.request_exposer.RequestExposerMiddleware'
]
```




