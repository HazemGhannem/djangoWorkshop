from django import forms
from users.models import Person
from .models import Events

CHOIX= (
        ('Musique','Musique'),
        ('Cinema','Cinema'),
        ('Sport','Sport'),
)
class EventForm(forms.ModelForm):
    title= forms.CharField(label='title')
    descripton=forms.CharField(label='desc',widget=forms.Textarea(attrs={
        'class':'form-control'
    }))
    image=forms.ImageField(label='img')
    category=forms.ChoiceField(label='category',choices=CHOIX,widget=forms.RadioSelect)
    nbe_participan=forms.IntegerField(min_value=0)
    evt_date=forms.DateField(label="date",
    widget=forms.DateInput(attrs={
            'type':'date',
            'class':'form-controll date-input'
    })
    )
    organizer=forms.ModelChoiceField(label='person',queryset=Person.objects.all())

    class Meta:
        model = Events
        fields = ['title','descripton','image','category','nbe_participan','organizer','evt_date']
       