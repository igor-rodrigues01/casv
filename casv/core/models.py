# -*- coding: utf-8 -*-
from django.contrib.gis.db import models
from django.contrib.auth.models import User


class Asv(models.Model):

    codigo = models.IntegerField(null=True, blank=True)
    n_autex = models.CharField('Número de Autorização de Extração',
        max_length=30, blank=True)
    uf = models.CharField('UF', max_length=2, blank=True)
    fito = models.CharField(max_length=60, blank=True)
    nom_prop = models.CharField('Nome do Proprietário',
        max_length=60, blank=True)
    cpfj_prop = models.CharField('CPF ou CNPJ do Proprietário',
        max_length=22, blank=True)
    detentor = models.CharField('Nome do Detentor', max_length=60, blank=True)
    cpfj_dete = models.CharField('CPF ou CNPJ do Detentor',
        max_length=22, blank=True)
    rt = models.CharField(max_length=60, blank=True)
    cpfj_rt = models.CharField(max_length=22, blank=True)
    area_ha = models.FloatField(null=True, blank=True)
    lenha_st = models.FloatField(null=True, blank=True)
    tora_m = models.FloatField(null=True, blank=True)
    torete_m = models.FloatField(null=True, blank=True)
    mourao_m = models.FloatField(null=True, blank=True)
    data_autex = models.DateField('Data de Autorização de Extração',
        null=True, blank=True)
    valido_ate = models.DateField('Data de Validade da Autorização',
        null=True, blank=True)
    municipio = models.CharField('Município', max_length=40, blank=True)

    usuario = models.ForeignKey(User)
    data_criacao = models.DateTimeField('Data de Criação', auto_now_add=True)

    geom = models.PolygonField(srid=4674)
    objects = models.GeoManager()

    def __str__(self):
        return '%s' % self.codigo

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Asv, self).save(*args, **kwargs)


class AreaSoltura(models.Model):

    processo = models.IntegerField(null=True, blank=True)
    nome = models.CharField('Nome da propriedade', max_length=255)
    endereco = models.CharField('Endereço', max_length=400)
    uf = models.CharField('Unidade da Federação', max_length=2)
    municipio = models.CharField('Município', max_length=255)
    proprietario = models.CharField('Nome do proprietário', max_length=255)
    cpf = models.BigIntegerField('CPF', null=True, blank=True)
    telefone = models.BigIntegerField(null=True, blank=True)
    email = models.EmailField()
    area = models.FloatField('Área da Propriedade (ha)', null=True, blank=True)
    arl_app = models.FloatField('Área de reserva legal e proteção permanente',
        null=True, blank=True)
    bioma = models.CharField('Bioma', max_length=255)
    fitofisionomia = models.CharField(max_length=255)
    conservacao = models.NullBooleanField()
    conectividade = models.NullBooleanField()
    uc = models.NullBooleanField()
    agua = models.NullBooleanField()
    atividade = models.CharField('Atividade Econômica', max_length=255)
    documento = models.NullBooleanField()
    mapa = models.NullBooleanField()
    carta = models.NullBooleanField()
    reabilitador = models.NullBooleanField()
    viveiro = models.IntegerField('Número de viveiros', null=True, blank=True)
    distancia = models.FloatField('Área da Propriedade (ha)')
    tempo = models.FloatField('Tempo de viagem ao CETAS mais próximo')
    vistoria = models.DateField()

    usuario = models.ForeignKey(User)
    data_criacao = models.DateTimeField('Data de Criação', auto_now_add=True)

    geom = models.PolygonField(srid=4674)
    objects = models.GeoManager()

    def __str__(self):
        return '%s' % self.processo


class AsvMataAtlantica(models.Model):

    processo = models.IntegerField()
    uf = models.CharField('Unidade da Federação', max_length=2)
    municipio = models.CharField('Município', max_length=255)
    empreendedor = models.CharField(max_length=255)
    tipo_empreendimento = models.CharField('Tipo de Empreendimento', max_length=255)
    cpfj = models.CharField('CPF ou CNPJ do Empreendedor', max_length=22, blank=True)
    area_supressao_total = models.FloatField('Área Total de Supressão (ha)')
    area_supressao_veg_primaria = models.FloatField("""Área de Supressão de
        Vegetação Primária (ha)""")
    area_supressao_estagio_medio = models.FloatField("""Área de Supressão em
        Estágio Médio (ha)""")
    area_supressao_estagio_avancado = models.FloatField("""Área de Supressão em
        Estágio Avançado (ha)""")

    usuario = models.ForeignKey(User)
    data_criacao = models.DateTimeField('Data de Criação', auto_now_add=True)

    geom = models.PolygonField(srid=4674)
    objects = models.GeoManager()

    def __str__(self):
        return '%s' % self.processo


class CompensacaoMataAtlantica(models.Model):

    processo = models.IntegerField()
    uf = models.CharField('Unidade da Federação', max_length=2)
    municipio = models.CharField('Município', max_length=255)
    empreendedor = models.CharField(max_length=255)
    tipo_empreendimento = models.CharField('Tipo de Empreendimento', max_length=255)
    cpfj = models.CharField('CPF ou CNPJ do Empreendedor', max_length=22, blank=True)
    area_compensacao = models.FloatField('Área de Compensação (ha)')

    usuario = models.ForeignKey(User)
    data_criacao = models.DateTimeField('Data de Criação', auto_now_add=True)

    geom = models.PolygonField(srid=4674)
    objects = models.GeoManager()

    def __str__(self):
        return '%s' % self.processo
