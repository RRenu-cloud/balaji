from django.db import models

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=100)
    description= models.TextField()
    img = models.ImageField(upload_to='madhu/')
    created_at = models.DateTimeField(auto_now_add=True)

    def  __str__(self):
        return self.name

    class Meta:
       verbose_name = 'Article'
       verbose_name_plural ='Articles'



