from django.db import models

# Create your models here.
class DataAnalizing(models.Model):
    id_node = models.IntegerField()
    localization = models.CharField(max_length=700)
    solar_radiaton = models.DecimalField(max_digits=12, decimal_places=3)
    wind_speed = models.DecimalField(max_digits=12, decimal_places=3)
    hour = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)

    def __int__(self):
        return self.id_node