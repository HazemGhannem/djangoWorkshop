from django.contrib import admin,messages
from .models import *
from datetime import date
# Register your models here.


class participationInline(admin.TabularInline): #or StackedInline
    model=Participation
    extra=1
    readonly_fields=('date_participation',)
    can_delete=True
class ParticipanFilter(admin.SimpleListFilter):
    title='Participation'
    parameter_name='nbe_participan'
    def lookups(self, request, model_admin) :
        return (
            ('0','0 Participation'),
            ('more','more Participation'),

        )
    def queryset(self, request, queryset) :
        if self.value()=='0':
            return  queryset.filter(nbe_participan__exact=0)
        if self.value == 'more':
            return queryset.filter(nbe_participan__gt=0)
class DateFilter(admin.SimpleListFilter):
    title='event date'
    parameter_name='evt_date'
    def lookups(self, request, model_admin) :
        return (
            ('Past Event','Old Events'),
            ('Today Event','Today Event'),
            ('Upcoming Event','Upcoming Event'),

        )
    def queryset(self, request, queryset) :
        if self.value()=='Past Event':
            return  queryset.filter(evt_date__lt=date.today())
        if self.value() == 'Today Event':
            return queryset.filter(evt_date__exact=date.today())
        if self.value() == 'Upcoming Event':
            return queryset.filter(evt_date__gt=date.today())


@admin.action(description='Mark state as False')
def UpdateState(modeladmin,request,queryset):
    rowsUpdated=queryset.update(state=False)
    if rowsUpdated :
        msg='one event'
    else:
        msg='more'
    return messages.success(request,message='%s Updated' %msg)
        

@admin.action(description='Mark state as True')
@admin.register(Events)
class EventAdmin(admin.ModelAdmin):
    def UpdateState2(self,request,queryset):
        rowsUpdated=queryset.update(state=True)
        if rowsUpdated :
         msg='one event'
        else:
            msg='more'
        return messages.success(request,message='%s Updated' %msg)

    def Participant_number(self,obj):
        val=obj.Participation.count()
        return val
    list_display =('title','category','state','Participant_number','created_at','evt_date',)
    list_filter =('category','state',ParticipanFilter,DateFilter)
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
    inlines=[participationInline]
    actions=[UpdateState,UpdateState2]
    #actions_on_bottom=True
    #actions_on_top=False
   
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


