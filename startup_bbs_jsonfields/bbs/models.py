from django.db import models

class Topic(models.Model):

    comment     = models.CharField(verbose_name="コメント",max_length=2000)

    def __str__(self):
        return self.comment



class Map(models.Model):

    data    = models.JSONField(verbose_name="マップデータ")



    



    


