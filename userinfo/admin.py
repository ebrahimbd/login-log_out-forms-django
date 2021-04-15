from django.contrib import admin


from . models import Savedata

admin.site.register(Savedata)



from . models import  Hotel
admin.site.register(Hotel)

from . models import  Author
admin.site.register(Author)
