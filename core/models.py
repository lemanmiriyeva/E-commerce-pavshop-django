from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True 


class Adress (models.Model):
    address = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = "adresses"
    

class Contanct_info (models.Model):
    address= models.ForeignKey(Adress, on_delete=models.CASCADE)
    phone = models.IntegerField()
    email_address = models.EmailField()
  

class ContactMessage (TimeStampedModel, models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.subject


class Team(TimeStampedModel, models.Model):
    img = models.ImageField(upload_to = 'TeamMembers_images' )
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.full_name


class Sponsor(TimeStampedModel, models.Model):
    img = models.ImageField(upload_to = 'sponsor_images')