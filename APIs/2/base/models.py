from django.db import models

# Create your models here.
class Prediction(models.Model):
    month1 = models.FloatField()
    month2 = models.FloatField()
    month3 = models.FloatField()
    month4 = models.FloatField()
    prediction_value = models.IntegerField(blank=True, null=True)

    def __int__(self):
        return self.prediction_value