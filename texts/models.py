from django.db import models

class Texts(models.Model):
    use_in_migrations = True
    textid = models.CharField(primary_key=True, max_length=10)
    regDate = models.DateField()

    class Meta:
        db_table="texts"

    def __str__(self):
        return f'{self.pk} {self.textid}'