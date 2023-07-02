from django.db import models


# Create your models here.
class Relatorio(models.Model):
    titulo = models.CharField(max_length=300)
    descricao = models.CharField(max_length=3000)
    tipo = models.CharField(choices=[('Noticia', 'Notícia' ), ('Pesquisa', 'Pesquisa'), 
                                     ('Outro', 'Outro'), ('Relatorio_de_audiencia', 'Relatório de audiência')], max_length=50)
    autor = models.CharField(max_length=30, null=True, blank=True)
    data = models.DateField()
    paragrafo1 = models.CharField(max_length=10000, null=True, blank=True)
    paragrafo2 = models.CharField(max_length=10000, null=True, blank=True)
    paragrafo3 = models.CharField(max_length=10000, null=True, blank=True)
    paragrafo4 = models.CharField(max_length=10000, null=True, blank=True)
    paragrafo5 = models.CharField(max_length=10000, null=True, blank=True)
    arquivo = models.FileField(upload_to='pdfs/', blank=True, null=True)
    imagem_thumb = models.ImageField(upload_to='images_thumb/', blank=True, null=True)
    imagem_post = models.ImageField(upload_to='images/', blank=True, null=True)
    legenda_imagem = models.CharField(max_length=300, blank=True, null=True)
    url = models.URLField(null=True, blank=True)

    class Meta:
        
        verbose_name_plural = 'relatorio'
        # permissions = [
        #     ("view_relatorio_list", "Can view relatorio list"),
        #  ]


class Programacao(models.Model):
    titulo = models.CharField(max_length=300)
    descricao = models.CharField(max_length=3000)
    tipo = models.CharField(choices=[('Programacao', 'Programação'), 
                                     ('Pipacast', 'Pipacast') ], max_length=50)
    subtipo = models.CharField(choices=[('pdf', 'pdf'), ('blog', 'blog')], max_length=50,
                               default='blog')
    
    autor = models.CharField(max_length=30, null=True, blank=True)
    data = models.DateField()
    paragrafo1 = models.CharField(max_length=10000, null=True, blank=True)
    paragrafo2 = models.CharField(max_length=10000, null=True, blank=True)
    paragrafo3 = models.CharField(max_length=10000, null=True, blank=True)
    paragrafo4 = models.CharField(max_length=10000, null=True, blank=True)
    paragrafo5 = models.CharField(max_length=10000, null=True, blank=True)
    arquivo = models.FileField(upload_to='pdfs/', blank=True, null=True)
    imagem_thumb = models.ImageField(upload_to='images_thumb/', blank=True, null=True)
    imagem_post = models.ImageField(upload_to='images/', blank=True, null=True)
    legenda_imagem = models.CharField(max_length=300, blank=True, null=True)
    link = models.CharField(max_length=300, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'programacoes'

    
class Carrossel(models.Model):
    imagem = models.ImageField(upload_to='images_carrossel/', blank=True, null=True)
    legenda_1 = models.CharField(max_length=200, blank=True, null=True)
    legenda_2 = models.CharField(max_length=200, blank=True, null=True)


    class Meta:
        verbose_name_plural = 'carrossel'
 