# -*- coding: utf-8 -*-tes
from django.contrib.gis.db import models
from django.contrib.auth.models import User


class AutoInfracaoOEMA(models.Model):

    proc = models.CharField(max_length=30, null=True, blank=True)
    num_ai = models.CharField(max_length=20, null=True, blank=True)
    num_tei = models.CharField(max_length=20, null=True, blank=True)
    area_ha = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    desc = models.CharField(max_length=2500, null=True, blank=True)
    legislacao = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    nome = models.CharField(max_length=100, null=True, blank=True)
    cpfj = models.CharField(max_length=20, null=True, blank=True)
    municipio = models.CharField(max_length=250, null=True, blank=True)
    geom = models.MultiPolygonField(srid=4674, null=True, blank=True)
    usuario = models.ForeignKey(User, related_name='infracao')
    data_criacao = models.DateTimeField('Data de Criação', auto_now_add=True)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Auto de Infração OEMA'
        verbose_name_plural = 'Autos de Infração OEMA'


class EmbargoOEMA(models.Model):

    proc = models.CharField(max_length=30, null=True, blank=True)
    num_ai = models.CharField(max_length=20, null=True, blank=True)
    num_tei = models.CharField(max_length=20, null=True, blank=True)
    area_ha = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    desc = models.CharField(max_length=2500, null=True, blank=True)
    legislacao = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    nome = models.CharField(max_length=100, null=True, blank=True)
    cpfj = models.CharField(max_length=20, null=True, blank=True)
    municipio = models.CharField(max_length=250, null=True, blank=True)
    geom = models.MultiPolygonField(srid=4674, null=True, blank=True)
    usuario = models.ForeignKey(User, related_name='embargo')
    data_criacao = models.DateTimeField('Data de Criação', auto_now_add=True)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'Embargo OEMA'
        verbose_name_plural = 'Embargos OEMA'


class Asv(models.Model):

    codigo = models.IntegerField(null=True, blank=True)
    n_autex = models.CharField(
        'Número de Autorização de Extração',
        max_length=30,
        null=True,
        blank=True)
    uf = models.CharField('UF', max_length=2, null=True, blank=True)
    fito = models.CharField(max_length=60, null=True, blank=True)
    nom_prop = models.CharField(
        'Nome do Proprietário',
        max_length=60,
        null=True,
        blank=True)
    cpfj_prop = models.CharField(
        'CPF ou CNPJ do Proprietário',
        max_length=22,
        null=True,
        blank=True)
    detentor = models.CharField(
        'Nome do Detentor',
        max_length=60,
        null=True,
        blank=True)
    cpfj_dete = models.CharField(
        'CPF ou CNPJ do Detentor',
        max_length=22,
        null=True,
        blank=True)
    rt = models.CharField(max_length=60, null=True, blank=True)
    cpfj_rt = models.CharField(max_length=22, null=True, blank=True)
    area_ha = models.FloatField('Área da Propriedade (ha)', null=True, blank=True)
    lenha_st = models.FloatField(null=True, blank=True)
    tora_m = models.FloatField(null=True, blank=True)
    torete_m = models.FloatField(null=True, blank=True)
    mourao_m = models.FloatField(null=True, blank=True)
    data_autex = models.DateField(
        'Data de Autorização de Extração',
        null=True,
        blank=True)
    valido_ate = models.DateField(
        'Data de Validade da Autorização',
        null=True,
        blank=True)
    municipio = models.CharField(
        'Município',
        max_length=40,
        null=True,
        blank=True)
    usuario = models.ForeignKey(User, related_name='asv')
    data_criacao = models.DateTimeField('Data de Criação', auto_now_add=True)
    geom = models.MultiPolygonField(srid=4674)
    objects = models.GeoManager()

    def __str__(self):
        return '%s' % self.codigo

    class Meta:
        verbose_name = 'Autorização de Supressão de Vegetação'
        verbose_name_plural = 'Autorizações de Supressão de Vegetação'


class AreaSoltura(models.Model):

    processo = models.IntegerField(null=True, blank=True)
    nome = models.CharField(
        'Nome da propriedade',
        max_length=255,
        null=True,
        blank=True)
    endereco = models.CharField(
        'Endereço',
        max_length=400,
        null=True,
        blank=True)
    uf = models.CharField(
        'Unidade da Federação',
        max_length=2,
        null=True,
        blank=True)
    municipio = models.CharField(
        'Município',
        max_length=255,
        null=True,
        blank=True)
    proprietario = models.CharField(
        'Nome do proprietário',
        max_length=255,
        null=True,
        blank=True)
    cpf = models.CharField('CPF', null=True, blank=True, max_length=11)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    area = models.FloatField('Área da Propriedade (ha)', null=True, blank=True)
    arl_app = models.FloatField(
        'Área de reserva legal e proteção permanente',
        null=True,
        blank=True)
    bioma = models.CharField('Bioma', max_length=255, null=True, blank=True)
    fitofisionomia = models.CharField(max_length=255, null=True, blank=True)
    taxon = models.CharField(max_length=255, null=True, blank=True)
    conservacao = models.NullBooleanField()
    conectividade = models.NullBooleanField()
    uc = models.NullBooleanField()
    agua = models.NullBooleanField()
    atividade = models.CharField(
        'Atividade Econômica',
        max_length=255,
        null=True,
        blank=True)
    documento = models.NullBooleanField()
    mapa = models.NullBooleanField()
    carta = models.NullBooleanField()
    reabilitador = models.NullBooleanField()
    viveiros = models.PositiveSmallIntegerField(
        'Número de viveiros',
        null=True,
        blank=True)
    distancia = models.FloatField(
        'Distância até o CETAS mais próximo',
        null=True,
        blank=True)
    tempo = models.CharField(
        'Tempo de viagem ao CETAS mais próximo',
        max_length=5,
        null=True,
        blank=True)
    vistoria = models.DateField(null=True, blank=True)
    usuario = models.ForeignKey(User, related_name='area_soltura')
    data_criacao = models.DateTimeField('Data de Criação', auto_now_add=True)
    geom = models.MultiPolygonField(srid=4674)
    objects = models.GeoManager()

    def __str__(self):
        return '%s' % self.processo

    class Meta:
        verbose_name = 'Área de Soltura de Animais Silvestres'
        verbose_name_plural = 'Áreas de Soltura de Animais Silvestres'


class DadosAnuenciaMataAtlantica(models.Model):
    
    processo = models.IntegerField(null=True, blank=True,unique=True)
    uf = models.CharField(
        'Unidade da Federação',
        max_length=2,
        null=True,
        blank=True)
    municipio = models.CharField(
        'Município',
        max_length=255,
        null=True,
        blank=True)
    empreendedor = models.CharField(max_length=255, null=True, blank=True)
    tipo_empreendimento = models.CharField(
        'Tipo de Empreendimento',
        max_length=255,
        null=True,
        blank=True)
    cpfj = models.CharField(
        'CPF ou CNPJ do Empreendedor',
        max_length=22,
        null=True,
        blank=True)
    area_empreendimento_total = models.FloatField(
        'Área Total de Empreendimento (ha)',
        null=True,
        blank=True)
    area_empreendimento_veg_primaria = models.FloatField(
        """Área Empreendida em Vegetação Primária (ha)""",
        null=True,
        blank=True)
    area_empreendimento_estagio_medio = models.FloatField(
        """Área de Empreendimento em Estágio Médio (ha)""",
        null=True,
        blank=True)
    area_empreendimento_estagio_avancado = models.FloatField(
        """Área de Empreendimento em Estágio Avançado (ha)""",
        null=True,
        blank=True)
    usuario      = models.ForeignKey(User, related_name='dadosanuencia')
    data_criacao = models.DateTimeField('Data de Criação', auto_now_add=True)
    objects      = models.GeoManager()
    urbano_metropolitano = models.CharField('Local Urbarno',max_length=5)
    status      = models.CharField('Status',max_length=30)
    observacao = models.TextField('Observação',null=True,blank=True)

    def __str__(self):
        return '%s' % self.processo

    class Meta:
        verbose_name = 'Dados de Anuência - Mata Atlântica'
        verbose_name_plural = 'Dados de Anuência - Mata Atlântica'


class GeomPedidoAnuenciaMataAtlantica(models.Model):
    
    processo = models.OneToOneField(DadosAnuenciaMataAtlantica,to_field='processo')
    geom     = models.MultiPolygonField(srid=4674)
    objects  = models.GeoManager()
    
    class Meta:
        verbose_name = 'Geometria do Pedido de Anuência - Mata Atlântica'
        verbose_name_plural = 'Geometrias dos Pedidos de Anuência - Mata Atlântica'


class GeomAnuenciaConcedidaMataAtlantica(models.Model):
    
    processo = models.OneToOneField(DadosAnuenciaMataAtlantica,to_field='processo')
    geom     = models.MultiPolygonField(srid=4674)
    objects  = models.GeoManager()
    
    class Meta:
        verbose_name = 'Geometria de Anuência Concedida - Mata Atlântica'
        verbose_name_plural = 'Geometrias das Anuências Concedidas'

# class PedidoAnuenciaMataAtlantica(models.Model):

#     processo = models.IntegerField(null=True, blank=True)
#     uf = models.CharField(
#         'Unidade da Federação',
#         max_length=2,
#         null=True,
#         blank=True)
#     municipio = models.CharField(
#         'Município',
#         max_length=255,
#         null=True,
#         blank=True)
#     empreendedor = models.CharField(max_length=255, null=True, blank=True)
#     tipo_empreendimento = models.CharField(
#         'Tipo de Empreendimento',
#         max_length=255,
#         null=True,
#         blank=True)
#     cpfj = models.CharField(
#         'CPF ou CNPJ do Empreendedor',
#         max_length=22,
#         null=True,
#         blank=True)
#     area_empreendimento_total = models.FloatField(
#         'Área Total de Empreendimento (ha)',
#         null=True,
#         blank=True)
#     area_empreendimento_veg_primaria = models.FloatField(
#         """Área Empreendida em Vegetação Primária (ha)""",
#         null=True,
#         blank=True)
#     area_empreendimento_estagio_medio = models.FloatField(
#         """Área de Empreendimento em Estágio Médio (ha)""",
#         null=True,
#         blank=True)
#     area_empreendimento_estagio_avancado = models.FloatField(
#         """Área de Empreendimento em Estágio Avançado (ha)""",
#         null=True,
#         blank=True)
#     usuario      = models.ForeignKey(User, related_name='pedanuencia')
#     data_criacao = models.DateTimeField('Data de Criação', auto_now_add=True)
#     geom         = models.MultiPolygonField(srid=4674)
#     objects      = models.GeoManager()
#     urbano_metropolitano = models.CharField('Local Urbarno',max_length=5)
#     observacao = models.TextField('Observação',null=True,blank=True) 

#     def __str__(self):
#         return '%s' % self.processo

#     class Meta:
#         verbose_name = 'Pedido de Anuência - Mata Atlântica'
#         verbose_name_plural = """ Pedidos de Anuência -
#             Mata Atlântica"""


# the difference in between 'AnuenciaConcedidaMataAtlantica' and
# 'PedidoAnuenciaMataAtlantica' is the field cpfj - cpf_cnpj
# class AnuenciaConcedidaMataAtlantica(models.Model):

#     processo = models.IntegerField(null=True, blank=True)
#     uf = models.CharField(
#         'Unidade da Federação',
#         max_length=2,
#         null=True,
#         blank=True)
#     municipio = models.CharField(
#         'Município',
#         max_length=255,
#         null=True,
#         blank=True)
#     empreendedor = models.CharField(max_length=255, null=True, blank=True)
#     tipo_empreendimento = models.CharField(
#         'Tipo de Empreendimento',
#         max_length=255,
#         null=True,
#         blank=True)
#     cpf_cnpj = models.CharField(
#         'CPF ou CNPJ do Empreendedor',
#         max_length=22,
#         null=True,
#         blank=True)
#     area_empreendimento_total = models.FloatField(
#         'Área Total de Empreendimento (ha)',
#         null=True,
#         blank=True)
#     area_empreendimento_veg_primaria = models.FloatField(
#         """Área Empreendida em Vegetação Primária (ha)""",
#         null=True,
#         blank=True)
#     area_empreendimento_estagio_medio = models.FloatField(
#         """Área de Empreendimento em Estágio Médio (ha)""",
#         null=True,
#         blank=True)
#     area_empreendimento_estagio_avancado = models.FloatField(
#         """Área de Empreendimento em Estágio Avançado (ha)""",
#         null=True,
#         blank=True)
#     usuario      = models.ForeignKey(User, related_name='anuenciaconcedida')
#     data_criacao = models.DateTimeField('Data de Criação', auto_now_add=True)
#     geom         = models.MultiPolygonField(srid=4674)
#     objects      = models.GeoManager()
#     urbano_metropolitano = models.CharField('Local Urbarno',max_length=5)
#     observacao = models.TextField('Observação',null=True,blank=True) 
#     def __str__(self):
#         return '%s' % self.processo

#     class Meta:
#         verbose_name = 'Anuência Concedida - Mata Atlântica'
#         verbose_name_plural = """Anuências Concedidas -
#             Mata Atlântica"""


class AsvMataAtlantica(models.Model):

    processo = models.IntegerField(null=True, blank=True)
    uf = models.CharField(
        'Unidade da Federação',
        max_length=2,
        null=True,
        blank=True)
    municipio = models.CharField(
        'Município',
        max_length=255,
        null=True,
        blank=True)
    empreendedor = models.CharField(max_length=255, null=True, blank=True)
    tipo_empreendimento = models.CharField(
        'Tipo de Empreendimento',
        max_length=255,
        null=True,
        blank=True)
    cpfj = models.CharField(
        'CPF ou CNPJ do Empreendedor',
        max_length=22,
        null=True,
        blank=True)
    area_supressao_total = models.FloatField(
        'Área Total de Supressão (ha)',
        null=True,
        blank=True)
    area_supressao_veg_primaria = models.FloatField(
        """Área de Supressão de Vegetação Primária (ha)""",
        null=True,
        blank=True)
    area_supressao_estagio_medio = models.FloatField(
        """Área de Supressão em Estágio Médio (ha)""",
        null=True,
        blank=True)
    area_supressao_estagio_avancado = models.FloatField(
        """Área de Supressão em Estágio Avançado (ha)""",
        null=True,
        blank=True)
    usuario = models.ForeignKey(User, related_name='asvma')
    data_criacao = models.DateTimeField('Data de Criação', auto_now_add=True)
    geom = models.MultiPolygonField(srid=4674)
    objects = models.GeoManager()

    def __str__(self):
        return '%s' % self.processo

    class Meta:
        verbose_name = 'Autorização de Supressão de Vegetação - Mata Atlântica'
        verbose_name_plural = """Autorizações de Supressão de Vegetação -
            Mata Atlântica"""


    def __str__(self):
        return '%s' % self.processo

    class Meta:
        verbose_name = 'Autorização de Supressão de Vegetação - Mata Atlântica'
        verbose_name_plural = """Autorizações de Supressão de Vegetação -
            Mata Atlântica"""


class CompensacaoMataAtlantica(models.Model):

    processo            = models.IntegerField(null=True, blank=True)
    uf                  = models.CharField(
        'Unidade da Federação',
        max_length=2,
        null=True,
        blank=True)
    municipio           = models.CharField(
        'Município',
        max_length=255,
        null=True,
        blank=True)
    empreendedor        = models.CharField(max_length=255, null=True,
        blank=True)
    tipo_empreendimento = models.CharField(
        'Tipo de Empreendimento',
        max_length=255,
        null=True,
        blank=True)
    cpfj                = models.CharField(
        'CPF ou CNPJ do Empreendedor',
        max_length=22,
        null=True,
        blank=True)
    area_compensacao_total = models.FloatField(
        'Área de Compensação (ha)',
        null=True,
        blank=True)
    usuario             = models.ForeignKey(User, related_name='compensacao')
    data_criacao        = models.DateTimeField('Data de Criação',
        auto_now_add=True)
    geom                = models.MultiPolygonField(srid=4674)
    objects             = models.GeoManager()
    tipo_compensacao    = models.CharField(max_length=12,null=True,blank=True)
    area_compensacao_veg_primaria     = models.FloatField(
        """Área de Compensação de Vegetação Primária (ha)""",
        null=True,
        blank=True)
    area_compensacao_estagio_inicial  = models.FloatField(
        """Área de Compensação em Estágio Inicial (ha)""",
        null=True,
        blank=True)
    area_compensacao_estagio_medio    = models.FloatField(
        """Área de Compensação em Estágio Médio (ha)""",
        null=True,
        blank=True)
    area_compensacao_estagio_avancado = models.FloatField(
        """Área de Compensação em Estágio Avançado (ha)""",
        null=True,
        blank=True) 
    observacao = models.TextField('Observação',null=True,blank=True)

    def __str__(self):
        return '%s' % self.processo

    class Meta:
        verbose_name = 'Área de Compensação - Mata Atlântica'
        verbose_name_plural = 'Áreas de Compensação - Mata Atlântica'

