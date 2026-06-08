from django.db import models

class CarMake(models.Model):
    name = models.CharField(max_index=True, max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=[('SUV', 'SUV'), ('Sedan', 'Sedan'), ('Wagon', 'Wagon')])
    year = models.IntegerField()

    def __str__(self):
        return f"{self.car_make.name} {self.name}"
