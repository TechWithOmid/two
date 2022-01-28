from django.core.exceptions import ObjectDoesNotExist
from .models import Writer


def writer_info(request):
    """ Create context processor for send writer_info.bio 
    to every view for showing in side bar """
    try:
        writer_info = Writer.objects.get(pk=1)
        return { "writer_info": writer_info }
    except ObjectDoesNotExist:
        return { "writer_info": "Nothing" }

