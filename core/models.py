import uuid
from django.db import models
from stdimage.models import StdImageField


ICON_CHOICES = (
    ('lni-cog', 'Engrenagem'),
    ('lni-stats-up', 'Gráfico'),
    ('lni-users', 'Usuário'),
    ('lni-layers', 'Design'),
    ('lni-mobile', 'Mobile'),
    ('lni-rocket', 'Foguete'),
    ('lni-laptop-phone', 'Computador&celular'),
    ('lni-leaf', 'Folha'),
    ('lni-package', 'Pacote'),
    ('lni-star', 'Estrela'),
    ('lni-drop', 'Gota'),
)


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    
    return filename


class Base(models.Model):
    created = models.DateField('Criação', auto_now_add=True)
    modified = models.DateField('Atualização', auto_now=True)
    active = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Service(Base):
    service = models.CharField('Serviço', max_length=100)
    description = models.TextField('Descrição', max_length=200)
    icon = models.CharField('Ícone', max_length=16, choices=ICON_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.service


class Position(Base):
    position = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.position


class Employee(Base):
    name = models.CharField('Nome', max_length=100)
    position = models.ForeignKey('core.Position', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    image = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb':{'width':480, 'height':480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.name


class Feature(Base):
    title = models.CharField('Título', max_length=100)
    icon = models.CharField('Ícone', max_length=16, choices=ICON_CHOICES)
    description = models.TextField('Descrição', max_length=300)


    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return self.title


class Plan(Base):
    name = models.CharField('Nome', max_length=100)
    icon = models.CharField('Ícone', max_length=16, choices=ICON_CHOICES)
    price = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    benefit1 = models.CharField('Benefício-1', max_length=100, default='benefício 1')
    benefit2 = models.CharField('Benefício-2', max_length=100, default='benefício 2')
    benefit3 = models.CharField('Benefício-3', max_length=100, default='benefício 3')
    benefit4 = models.CharField('Benefício-4', max_length=100, default='benefício 4')

    class Meta:
        verbose_name = 'Plano'
        verbose_name_plural = 'Planos'

    def __str__(self):
        return self.name


class Client(Base):
    name = models.CharField('Nome', max_length=100)
    img = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb':{'width':75, 'height':75, 'crop': True}}, default=False)
    occupation = models.ForeignKey('core.Position', verbose_name='Profissão', on_delete=models.CASCADE)
    description = models.TextField('Descrição', max_length=300)
    rating = models.PositiveSmallIntegerField('Avaliação')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.name

