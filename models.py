from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    coins = models.IntegerField()


class Game(models.Model):
    game_id = models.IntegerField()
    playersCount = models.IntegerField()


class Hand(models.Model):
    name = models.CharField(max_length=100)
    hand = models.IntegerField()
