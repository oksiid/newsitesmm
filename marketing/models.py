from django.db import models

#аватар, чат календарь задача дедлайны

class Company(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=100, blank=True)
    active = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='avatar', blank=True)

    def __str__(self):
        return self.name

class Work(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    tast = models.CharField(max_length=100)
    date = models.DateTimeField()
