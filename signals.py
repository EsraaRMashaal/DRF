from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=None)
def set_param(sender, instance, **kwargs):
    if instance:
        try: 
            param_id = models.exposed_request.META.get("HTTP_Param_ID")
            if hasattr(instance, 'param'):
                instance.param_id = param_id
                instance.save()
        except:
            print("exposed_request is not exist")
     
    
