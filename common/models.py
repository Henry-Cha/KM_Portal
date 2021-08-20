from django.db import models


class Coordinate(models.Model):
    latitude = models.CharField(max_length=20)         # 위도
    longitude = models.CharField(max_length=20)        # 경도