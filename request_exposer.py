from django.apps import apps

# to be able to access request object in models
def RequestExposerMiddleware(get_response):
    def middleware(request):
        # get all models in all apps and add request object to them
        for app in apps.get_app_configs():
            if app.models_module:
                app.models_module.exposed_request = request
            
        response = get_response(request)
        return response

    return middleware
