# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Asv.typology'
        db.delete_column(u'core_asv', 'typology')

        # Deleting field 'Asv.reservator'
        db.delete_column(u'core_asv', 'reservator')

        # Deleting field 'Asv.n_proc'
        db.delete_column(u'core_asv', 'n_proc')

        # Adding field 'Asv.n_autex'
        db.add_column(u'core_asv', 'n_autex',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True),
                      keep_default=False)

        # Adding field 'Asv.uf'
        db.add_column(u'core_asv', 'uf',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=2, blank=True),
                      keep_default=False)

        # Adding field 'Asv.fito'
        db.add_column(u'core_asv', 'fito',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=60, blank=True),
                      keep_default=False)

        # Adding field 'Asv.nom_prop'
        db.add_column(u'core_asv', 'nom_prop',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=60, blank=True),
                      keep_default=False)

        # Adding field 'Asv.cpfj_prop'
        db.add_column(u'core_asv', 'cpfj_prop',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=22, blank=True),
                      keep_default=False)

        # Adding field 'Asv.detentor'
        db.add_column(u'core_asv', 'detentor',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=60, blank=True),
                      keep_default=False)

        # Adding field 'Asv.cpfj_dete'
        db.add_column(u'core_asv', 'cpfj_dete',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=22, blank=True),
                      keep_default=False)

        # Adding field 'Asv.rt'
        db.add_column(u'core_asv', 'rt',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=60, blank=True),
                      keep_default=False)

        # Adding field 'Asv.cpfj_rt'
        db.add_column(u'core_asv', 'cpfj_rt',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=22, blank=True),
                      keep_default=False)

        # Adding field 'Asv.lenha_st'
        db.add_column(u'core_asv', 'lenha_st',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Adding field 'Asv.tora_m'
        db.add_column(u'core_asv', 'tora_m',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Adding field 'Asv.torete_m'
        db.add_column(u'core_asv', 'torete_m',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Adding field 'Asv.mourao_m'
        db.add_column(u'core_asv', 'mourao_m',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Adding field 'Asv.data_autex'
        db.add_column(u'core_asv', 'data_autex',
                      self.gf('django.db.models.fields.DateField')(null=True),
                      keep_default=False)

        # Adding field 'Asv.valido_ate'
        db.add_column(u'core_asv', 'valido_ate',
                      self.gf('django.db.models.fields.DateField')(null=True),
                      keep_default=False)

        # Adding field 'Asv.municipio'
        db.add_column(u'core_asv', 'municipio',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=40, blank=True),
                      keep_default=False)


        # Changing field 'Asv.code'
        db.alter_column(u'core_asv', 'code', self.gf('django.db.models.fields.IntegerField')(max_length=6, null=True))

        # Changing field 'Asv.area_ha'
        db.alter_column(u'core_asv', 'area_ha', self.gf('django.db.models.fields.FloatField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Asv.typology'
        raise RuntimeError("Cannot reverse this migration. 'Asv.typology' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Asv.typology'
        db.add_column(u'core_asv', 'typology',
                      self.gf('django.db.models.fields.CharField')(max_length=30),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Asv.reservator'
        raise RuntimeError("Cannot reverse this migration. 'Asv.reservator' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Asv.reservator'
        db.add_column(u'core_asv', 'reservator',
                      self.gf('django.db.models.fields.CharField')(max_length=3),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Asv.n_proc'
        raise RuntimeError("Cannot reverse this migration. 'Asv.n_proc' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Asv.n_proc'
        db.add_column(u'core_asv', 'n_proc',
                      self.gf('django.db.models.fields.CharField')(max_length=19),
                      keep_default=False)

        # Deleting field 'Asv.n_autex'
        db.delete_column(u'core_asv', 'n_autex')

        # Deleting field 'Asv.uf'
        db.delete_column(u'core_asv', 'uf')

        # Deleting field 'Asv.fito'
        db.delete_column(u'core_asv', 'fito')

        # Deleting field 'Asv.nom_prop'
        db.delete_column(u'core_asv', 'nom_prop')

        # Deleting field 'Asv.cpfj_prop'
        db.delete_column(u'core_asv', 'cpfj_prop')

        # Deleting field 'Asv.detentor'
        db.delete_column(u'core_asv', 'detentor')

        # Deleting field 'Asv.cpfj_dete'
        db.delete_column(u'core_asv', 'cpfj_dete')

        # Deleting field 'Asv.rt'
        db.delete_column(u'core_asv', 'rt')

        # Deleting field 'Asv.cpfj_rt'
        db.delete_column(u'core_asv', 'cpfj_rt')

        # Deleting field 'Asv.lenha_st'
        db.delete_column(u'core_asv', 'lenha_st')

        # Deleting field 'Asv.tora_m'
        db.delete_column(u'core_asv', 'tora_m')

        # Deleting field 'Asv.torete_m'
        db.delete_column(u'core_asv', 'torete_m')

        # Deleting field 'Asv.mourao_m'
        db.delete_column(u'core_asv', 'mourao_m')

        # Deleting field 'Asv.data_autex'
        db.delete_column(u'core_asv', 'data_autex')

        # Deleting field 'Asv.valido_ate'
        db.delete_column(u'core_asv', 'valido_ate')

        # Deleting field 'Asv.municipio'
        db.delete_column(u'core_asv', 'municipio')


        # User chose to not deal with backwards NULL issues for 'Asv.code'
        raise RuntimeError("Cannot reverse this migration. 'Asv.code' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Asv.code'
        db.alter_column(u'core_asv', 'code', self.gf('django.db.models.fields.IntegerField')(max_length=10))

        # User chose to not deal with backwards NULL issues for 'Asv.area_ha'
        raise RuntimeError("Cannot reverse this migration. 'Asv.area_ha' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Asv.area_ha'
        db.alter_column(u'core_asv', 'area_ha', self.gf('django.db.models.fields.FloatField')())

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.asv': {
            'Meta': {'object_name': 'Asv'},
            'area_ha': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'code': ('django.db.models.fields.IntegerField', [], {'max_length': '6', 'null': 'True'}),
            'cpfj_dete': ('django.db.models.fields.CharField', [], {'max_length': '22', 'blank': 'True'}),
            'cpfj_prop': ('django.db.models.fields.CharField', [], {'max_length': '22', 'blank': 'True'}),
            'cpfj_rt': ('django.db.models.fields.CharField', [], {'max_length': '22', 'blank': 'True'}),
            'data_autex': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'detentor': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'fito': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lenha_st': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'mourao_m': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'municipio': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'n_autex': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'nom_prop': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'polygon': ('django.contrib.gis.db.models.fields.PolygonField', [], {'srid': '4674'}),
            'rt': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'tora_m': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'torete_m': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'uf': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'valido_ate': ('django.db.models.fields.DateField', [], {'null': 'True'})
        }
    }

    complete_apps = ['core']