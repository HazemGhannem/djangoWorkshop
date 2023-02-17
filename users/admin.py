from django.contrib import admin
from .models import Person
from .models import *

# Register your models here.
@admin.register(Person)
class personAdmin(admin.ModelAdmin):
    def event(self,obj):
        val=obj.participations.filter()
        #TODO
        
        print(val)
        #print(dir(val))
        return val

    list_display =('cin','email','username','is_staff','is_active','event')
    list_filter =('email','username')
    search_fields=['email','username']
    list_per_page= 5
    ordering=('email','username')
    #readonly_fields=('email','username')
    #autocomplete_fields=['organizer']
    fieldsets =(
        
        ('Person Info ' , {
            'classes' :('collapse',),
            'fields' :('cin','username','email','is_staff')
            }) ,    
    )
   

#admin.site.register(Person,PersonAdmin)


