from django.db import models

# Create your models here.


#parent model
class forum(models.Model):




    def __str__(self):
        return str(self.topic)

    

#child model
class Discussion(models.Model):
    

    def __str__(self):
        return str(self.forum)





        