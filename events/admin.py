from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Events)


class EventAdmin(admin.ModelAdmin):


    def Participant_number(self,obj):
        val=obj.Participation.count()
        return val
    list_display =('title','category','state','Participant_number','created_at','evt_date',)
    list_filter =('category','state')
    search_fields=['title','category']
    list_per_page= 5
    ordering=('-title','-created_at','evt_date',)
    readonly_fields=('updated_at','created_at')
    autocomplete_fields=['organizer']
    fieldsets =(
        
        ('Event State' , {
            
            'fields' :('state',)

            
            }) ,
        
        ('About' ,
         {   'classes' :('collapse',),
             'fields' :('title','descripton','image','category','nbe_participan','organizer')
         }
          ),
        ('Dates',
         { 'classes' :('collapse',),
             'fields' :('evt_date','updated_at','created_at')
         }
         )
        
        
        
        
    )
   
class ParticipationAdmin(admin.ModelAdmin):
    def person_Email(self,obj):
        val=obj.Person.email
        return val
    def person_Username(self,obj):
        val=obj.Person.username
        return val
    def Event_Title(self,obj):
        val=obj.event.title
        return val
    def Event_Category(self,obj):
        val=obj.event.category
        return val
    list_display =('person_Username','person_Email','Event_Title','Event_Category','date_participation')
    list_filter =('Person','event')
    search_fields=['Person','event']
    list_per_page= 5
    ordering=('Person','event')
admin.site.register(Participation,ParticipationAdmin)


