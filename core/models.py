from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class LGA(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="lgas")
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ("state", "name")
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}, {self.state.name}"


class Ward(models.Model):
    lga = models.ForeignKey(LGA, on_delete=models.CASCADE, related_name="wards")
    name = models.CharField(max_length=150)

    class Meta:
        unique_together = ("lga", "name")

    def __str__(self):
        return f"{self.name} ({self.lga})"


class City(models.Model):
    lga = models.ForeignKey(LGA, on_delete=models.CASCADE, related_name="cities")
    name = models.CharField(max_length=150)

    class Meta:
        unique_together = ("lga", "name")

    def __str__(self):
        return f"{self.name}, {self.lga.state.name}"


class PostalCode(models.Model):
    code = models.CharField(max_length=10)
    lga = models.ForeignKey(LGA, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        unique_together = ("code", "lga")

    def __str__(self):
        return self.code
