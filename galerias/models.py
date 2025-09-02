from django.db import models

# Create your models here.
class Galeria(models.Model):
    image1 = models.ImageField(upload_to='galerias/images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='galerias/images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='galerias/images/', blank=True, null=True)
    car = models.CharField(max_length=200)
    description1 = models.TextField()
    # title = models.CharField(max_length=200)
    # description = models.TextField()
    # ingredients = models.TextField()
    # instructions = models.TextField()
    # # Campo para a imagem da receita
    # image = models.ImageField(upload_to='galerias/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now = True)
    # car2 = models.CharField(max_length=200)
    # description2 = models.TextField()
    # car3 = models.CharField(max_length=200)
    # description3 = models.TextField()

    def __str__(self):
        return self.car

    class Meta:
        verbose_name = "Galeria"
        verbose_name_plural = "Galerias"
        ordering = ['-created_at'] # Ordena as receitas pela data de criação (mais novas primeiro)