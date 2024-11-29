from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
# número cartão
#cpf do usuário
#nome do usário igual aparece no cartão
# código de validação
#data de vencimento do cartão

class Validar(models.Model):
    id_validar = models.AutoField(primary_key=True)
    cartao_validar =models.CharField(max_length=255 ,null=False)
    cpf_validar =models.CharField(max_length=255 ,null=False)
    nome_validar =models.CharField(max_length=255 ,null=False)
    codigo_validar =models.CharField(max_length=255 ,null=False)
    data_validar =models.CharField(max_length=255 ,null=False)

    def __str__(self):
        return self.nome_validar
