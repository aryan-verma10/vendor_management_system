from django.db import models
from datetime import time

class CommonModel(models.Model):
    '''
        Common model contains common fields required in each model
    '''
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    deleted_at = models.DateTimeField(null = True, blank = True)

    class Meta:
        abstract = True




def converting_seconds_to_timefield_format(seconds: float):
    '''
        Utility function to convert seconds to hr:minutes:seconds
    '''
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    

    converted_time = time(int(hours), int(minutes), int(seconds))
    return converted_time



    