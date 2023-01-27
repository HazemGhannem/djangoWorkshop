from django.db import models

# Create your models here.

class Events(models.Model ):
    titre= models.CharField(max_length=50)
    descripton= models.TextField()
    image= models.ImageField()
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


