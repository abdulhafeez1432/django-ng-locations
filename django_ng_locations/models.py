from django.db import models


class Zone(models.Model):
    """
    Represents the 6 geopolitical zones of Nigeria
    """
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Geopolitical Zone"
        verbose_name_plural = "Geopolitical Zones"

    def __str__(self):
        return self.name


class State(models.Model):
    """
    Represents the 36 states of Nigeria plus FCT
    """
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name="states")
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, blank=True)
    capital = models.CharField(max_length=100, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "State"
        verbose_name_plural = "States"

    def __str__(self):
        return self.name


class LGA(models.Model):
    """
    Represents Local Government Areas (LGAs) in Nigeria
    """
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="lgas")
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, blank=True)

    class Meta:
        unique_together = ("state", "name")
        ordering = ["name"]
        verbose_name = "Local Government Area"
        verbose_name_plural = "Local Government Areas"

    def __str__(self):
        return f"{self.name}, {self.state.name}"


class City(models.Model):
    """
    Represents cities and towns in Nigeria
    """
    lga = models.ForeignKey(LGA, on_delete=models.CASCADE, related_name="cities")
    name = models.CharField(max_length=150)
    is_capital = models.BooleanField(default=False)
    population = models.IntegerField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ("lga", "name")
        ordering = ["name"]
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return f"{self.name}, {self.lga.state.name}"


class Ward(models.Model):
    """
    Represents electoral/administrative wards in Nigeria
    """
    lga = models.ForeignKey(LGA, on_delete=models.CASCADE, related_name="wards")
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=50, blank=True)

    class Meta:
        unique_together = ("lga", "name")
        ordering = ["name"]
        verbose_name = "Ward"
        verbose_name_plural = "Wards"

    def __str__(self):
        return f"{self.name} ({self.lga})"


class PostalCode(models.Model):
    """
    Represents postal codes in Nigeria
    """
    code = models.CharField(max_length=10, unique=True)
    lga = models.ForeignKey(LGA, on_delete=models.CASCADE, related_name="postal_codes")
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, null=True, blank=True, related_name="postal_codes"
    )
    area = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["code"]
        verbose_name = "Postal Code"
        verbose_name_plural = "Postal Codes"

    def __str__(self):
        return f"{self.code} - {self.area if self.area else self.lga.name}"

