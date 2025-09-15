from django.db import models

class Mutualist(models.Model):
    """This class represent a mutualist"""
    first_name = models.CharField("Prenoms", max_length=100)
    last_name = models.CharField("Nom", max_length=25)
    phone_number = models.CharField("Numero", max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Mutualiste"
        verbose_name_plural = "Mutualistes"
        ordering = ["last_name"]


class Sms(models.Model):
    """This class represent a SMS to send to a mutualist"""
    content = models.TextField()
    mutualists = models.ManyToManyField(Mutualist)

    def __str__(self):
        return f"sms n°{self.id}"
    
    
    class Meta:
        verbose_name = "SMS"
        verbose_name_plural = "SMS"
    
