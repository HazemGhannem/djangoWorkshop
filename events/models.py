from django.db import models
from users.models import Person
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from datetime import date

# Create your models here.
def title_valid(val):
    if not val[0].isupper():      
        raise  ValidationError("le titre doit commencer par une majuscule")
    return

class Events(models.Model ):
    title= models.CharField(max_length=50, validators=[title_valid])
    descripton= models.TextField()
    image= models.ImageField(upload_to='Image')
    CHOIX= (
        ('Musique','Musique'),
        ('Cinema','Cinema'),
        ('Sport','Sport'),
    )
    category = models.CharField(max_length=10,choices=CHOIX)
    state= models.BooleanField(default=False)
    nbe_participan= models.IntegerField(
        default=0,
        validators=[MinValueValidator(limit_value=0,message='le nombre de participant doit être positif')]
        )
    
    evt_date= models.DateField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #relation 
    organizer = models.ForeignKey(Person,on_delete=models.CASCADE)
    Participation = models.ManyToManyField(
        Person,
        through='Participation',
        related_name='participations'

    )
    def __str__(self):
        return f" {self.title} {self.category}"
    class Meta:
        constraints =[
            models.CheckConstraint(
                check=models.Q(
                   evt_date__gte= date.today() 
                ),
                name='the event date is invalid'
                
                ),
        ]
        verbose_name =('Evenement')
        verbose_name_plural ='Evenements'


class Participation(models.Model):
    Person = models.ForeignKey(Person,on_delete=models.CASCADE)
    event = models.ForeignKey(Events,on_delete=models.CASCADE)
    date_participation = models.DateTimeField(auto_now_add=True)


