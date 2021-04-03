import uuid
from django.db import models
from stdimage.models import StdImageField
from django.utils.translation import gettext_lazy as _


ICON_CHOICES = (
    ('lni-cog', _('Engrenagem')),
    ('lni-stats-up', _('Gráfico')),
    ('lni-users', _('Usuário')),
    ('lni-layers', _('Design')),
    ('lni-mobile', _('Mobile')),
    ('lni-rocket', _('Foguete')),
    ('lni-laptop-phone', _('Computador&celular')),
    ('lni-leaf', _('Folha')),
    ('lni-package', _('Pacote')),
    ('lni-star', _('Estrela')),
    ('lni-drop', _('Gota')),
)


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    
    return filename


class Base(models.Model):
    created = models.DateField(_('Criação'), auto_now_add=True)
    modified = models.DateField(_('Atualização'), auto_now=True)
    active = models.BooleanField(_('Ativo?'), default=True)

    class Meta:
        abstract = True


class Service(Base):
    service = models.CharField(_('Serviço'), max_length=100)
    description = models.TextField(_('Descrição'), max_length=200)
    icon = models.CharField(_('Ícone'), max_length=16, choices=ICON_CHOICES)

    class Meta:
        verbose_name = _('Serviço')
        verbose_name_plural = _('Serviços')

    def __str__(self):
        return self.service


class Position(Base):
    position = models.CharField(_('Cargo'), max_length=100)

    class Meta:
        verbose_name = _('Cargo')
        verbose_name_plural = _('Cargos')

    def __str__(self):
        return self.position


class Employee(Base):
    name = models.CharField(_('Nome'), max_length=100)
    position = models.ForeignKey('core.Position', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField(_('Bio'), max_length=200)
    image = StdImageField(_('Imagem'), upload_to=get_file_path, variations={'thumb':{'width':480, 'height':480, 'crop': True}})
    facebook = models.CharField(_('Facebook'), max_length=100, default='#')
    twitter = models.CharField(_('Twitter'), max_length=100, default='#')
    instagram = models.CharField(_('Instagram'), max_length=100, default='#')

    class Meta:
        verbose_name = _('Funcionário')
        verbose_name_plural = _('Funcionários')

    def __str__(self):
        return self.name


class Feature(Base):
    title = models.CharField(_('Título'), max_length=100)
    icon = models.CharField(_('Ícone'), max_length=16, choices=ICON_CHOICES)
    description = models.TextField(_('Descrição'), max_length=300)


    class Meta:
        verbose_name = _('Feature')
        verbose_name_plural = _('Features')

    def __str__(self):
        return self.title


class Plan(Base):
    name = models.CharField(_('Nome'), max_length=100)
    icon = models.CharField(_('Ícone'), max_length=16, choices=ICON_CHOICES)
    price = models.DecimalField(_('Preço'), max_digits=8, decimal_places=2)
    benefit1 = models.CharField(_('Benefício-1'), max_length=100, default='benefício 1')
    benefit2 = models.CharField(_('Benefício-2'), max_length=100, default='benefício 2')
    benefit3 = models.CharField(_('Benefício-3'), max_length=100, default='benefício 3')
    benefit4 = models.CharField(_('Benefício-4'), max_length=100, default='benefício 4')

    class Meta:
        verbose_name = _('Plano')
        verbose_name_plural = _('Planos')

    def __str__(self):
        return self.name


class Client(Base):
    name = models.CharField(_('Nome'), max_length=100)
    img = StdImageField(_('Imagem'), upload_to=get_file_path, variations={'thumb':{'width':75, 'height':75, 'crop': True}}, default=False)
    occupation = models.ForeignKey('core.Position', verbose_name='Profissão', on_delete=models.CASCADE)
    description = models.TextField('Descrição', max_length=300)
    rating = models.PositiveSmallIntegerField(_('Avaliação'))

    class Meta:
        verbose_name = _('Cliente')
        verbose_name_plural = _('Clientes')

    def __str__(self):
        return self.name

