from django.db import models

# Create your models here.
from django.urls import reverse



class Evidence(models.Model):
    """Model representing a Crime evidence(not specific copy of evidence)."""
    evi_case = models.ForeignKey('Evi_case', on_delete=models.SET_NULL, null=True)
    evi_number = models.CharField(max_length=10)
    evi_type = models.ForeignKey('Evi_type', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, null=True, help_text = 'Enter brief description of evidence')
    evi_time = models.DateTimeField(null=True, blank=True)
    signiture = models.ImageField(blank=True, null=True,
            upload_to="signitures/")
    picture = models.ImageField(blank=True, null=True,
            upload_to="pictures/")

    record = models.FileField(blank=True, null=True,
            upload_to="records/")

    def __str__(self):
        """String for representing the Model object."""
        return self.evi_number
    def get_absolute_url(self):
        return reverse('evidence-detail', args=[str(self.id)])



class Evi_type(models.Model):
    """Model representing evidence type."""
    name = models.CharField(max_length=200, help_text = 'Enter a evidence type(e.g. fingerprint)')

    class Meta:
        ordering = ['name']


    def get_absolute_url(self):
        """Returns the url to access a particular crime type."""
        return reverse('type-detail', args=[str(self.id)])


    def __str__(self):
        """String for representing the Model object."""
        return self.name



class Evi_case(models.Model):
    """Model representing evidence case."""
    number = models.PositiveIntegerField()
    summary = models.TextField(max_length=1000, null = True)
    class Meta:
        ordering = ['number']

 
    def get_absolute_url(self):
        """Returns the url to access a particular crime type."""
        return reverse('case-detail', args=[str(self.id)])


    def __str__(self):
        """String for representing the Model object."""
        return str(self.number)

