from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')

    def __str__(self):
        return self.name


class Coach(models.Model):
    name = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='coaches')

    def __str__(self):
        return self.name


class Manager(models.Model):
    name = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='managers')

    def __str__(self):
        return self.name


class Fixture(models.Model):
    team1 = models.OneToOneField(Team, on_delete=models.CASCADE, related_name="+")
    team2 = models.OneToOneField(Team, on_delete=models.CASCADE, related_name="+")
    team1_score = models.IntegerField()
    team2_score = models.IntegerField()
    datetime = models.DateTimeField()

    def __str__(self):
        return self.name
