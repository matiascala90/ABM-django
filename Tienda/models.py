from django.db import models

# Create your models here.
#Compania
class Compania(models.Model):
    nombre_compania=models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre_compania
    
#Plataforma
class Plataforma(models.Model):
    nombre_plataforma=models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre_plataforma

        
class Genero(models.Model):
    nombre_genero=models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre_genero    
    
 #Juegos   
class Juego(models.Model):
    titulo=models.CharField(max_length=255)
    foto= models.ImageField(upload_to='imagenes',default='imagen')
    compania=models.ForeignKey(Compania,on_delete=models.CASCADE)
    plataforma=models.ForeignKey(Plataforma,on_delete=models.CASCADE)
    genero=models.ForeignKey(Genero,on_delete=models.CASCADE)
    precio=models.FloatField()
    
    def __str__(self):
        return self.titulo   
