from django.db import models
from users.models import Person

# Create your models here.


class Events(models.Model ):
    titre= models.CharField(max_length=50)
    descripton= models.TextField()
    image= models.ImageField(upload_to='Image')
    CHOIX= (
        ('Musique','Musique'),
        ('Cinema','Cinema'),
        ('Sport','Sport'),
    )
    category = models.CharField(max_length=10,choices=CHOIX)
    state= models.BinaryField(default=False)
    nbe_participan= models.IntegerField(default=0)
    evt_date= models.DateField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #relation 
    organize = models.ForeignKey(Person,on_delete=models.CASCADE)
    Participation = models.ManyToManyField(
        Person,
        through='Participation',
        related_name='participations'

    )


class Participation(models.Model):
    Person = models.ForeignKey(Person,on_delete=models.CASCADE)
    event = models.ForeignKey(Events,on_delete=models.CASCADE)
    date_participation = models.DateTimeField(auto_now_add=True)


