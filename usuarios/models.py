from django.db.models import signals
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
from stdimage.models import StdImageField
from enum import unique
from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    
    use_in_migrations: True
    
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')
        
        return self._create_user(email, password, **extra_fields)
    
class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    fone = models.CharField('Telefone', max_length=15)
    is_staff = models.BooleanField('Membro da equipe', default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'fone']
    
    def __str__(self):
        return self.email
    
    objects= UsuarioManager()
    
    
class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now_add=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('preço', max_digits=8, decimal_places=2)
    estoque = models.DecimalField('Estoque', max_digits=8, decimal_places=3)
    imagem = StdImageField('imagem', upload_to='produtos',
                           variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome


def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(produto_pre_save, sender=Produto)

        