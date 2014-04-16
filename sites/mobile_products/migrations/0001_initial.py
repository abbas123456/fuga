# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Artist'
        db.create_table(u'mobile_products_artist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('biography', self.gf('django.db.models.fields.TextField')()),
            ('is_primary', self.gf('django.db.models.fields.BooleanField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'mobile_products', ['Artist'])

        # Adding model 'AttachmentFile'
        db.create_table(u'mobile_products_attachmentfile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('crc32_checksum', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('size', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'mobile_products', ['AttachmentFile'])

        # Adding model 'Attachment'
        db.create_table(u'mobile_products_attachment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('attachment_type', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('original_file_name', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('attachment_file', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mobile_products.AttachmentFile'], unique=True)),
        ))
        db.send_create_signal(u'mobile_products', ['Attachment'])

        # Adding model 'CoverArt'
        db.create_table(u'mobile_products_coverart', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('color_model', self.gf('django.db.models.fields.CharField')(default='RGB', max_length=8)),
            ('width', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('file_format', self.gf('django.db.models.fields.CharField')(default='JPEG', max_length=8)),
            ('attachment_file', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mobile_products.AttachmentFile'], unique=True)),
        ))
        db.send_create_signal(u'mobile_products', ['CoverArt'])

        # Adding model 'Contributor'
        db.create_table(u'mobile_products_contributor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'mobile_products', ['Contributor'])

        # Adding model 'Publisher'
        db.create_table(u'mobile_products_publisher', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('publisher', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('writer', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'mobile_products', ['Publisher'])

        # Adding model 'AudioResource'
        db.create_table(u'mobile_products_audioresource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recording_type', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('duration', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('resource_file', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mobile_products.AttachmentFile'])),
        ))
        db.send_create_signal(u'mobile_products', ['AudioResource'])

        # Adding model 'VideoResource'
        db.create_table(u'mobile_products_videoresource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file_format', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('encoding', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('bitrate', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('dimensions', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('fps', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('resource_file', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mobile_products.AttachmentFile'])),
        ))
        db.send_create_signal(u'mobile_products', ['VideoResource'])

        # Adding model 'UsageRight'
        db.create_table(u'mobile_products_usageright', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'mobile_products', ['UsageRight'])

        # Adding model 'Ringtone'
        db.create_table(u'mobile_products_ringtone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alternate_genre', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('alternate_subgenre', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('available_separately', self.gf('django.db.models.fields.BooleanField')()),
            ('catalog_tier', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('country_of_commissioning', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('country_of_recording', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('display_artist', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('duration', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('isrc_code', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('lyrics', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('main_genre', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('main_subgenre', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('parental_advisory', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('publishing_rights_owner', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('publishing_rights_year', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('recording_location', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('recording_year', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('rights_contract_begin_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('rights_holder_name', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('rights_ownership_name', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('sequence_number', self.gf('django.db.models.fields.IntegerField')()),
            ('suggested_preview_length', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('suggested_preview_start', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
        ))
        db.send_create_signal(u'mobile_products', ['Ringtone'])

        # Adding M2M table for field artists on 'Ringtone'
        m2m_table_name = db.shorten_name(u'mobile_products_ringtone_artists')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ringtone', models.ForeignKey(orm[u'mobile_products.ringtone'], null=False)),
            ('artist', models.ForeignKey(orm[u'mobile_products.artist'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ringtone_id', 'artist_id'])

        # Adding M2M table for field contributors on 'Ringtone'
        m2m_table_name = db.shorten_name(u'mobile_products_ringtone_contributors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ringtone', models.ForeignKey(orm[u'mobile_products.ringtone'], null=False)),
            ('contributor', models.ForeignKey(orm[u'mobile_products.contributor'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ringtone_id', 'contributor_id'])

        # Adding M2M table for field publishers on 'Ringtone'
        m2m_table_name = db.shorten_name(u'mobile_products_ringtone_publishers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ringtone', models.ForeignKey(orm[u'mobile_products.ringtone'], null=False)),
            ('publisher', models.ForeignKey(orm[u'mobile_products.publisher'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ringtone_id', 'publisher_id'])

        # Adding M2M table for field audio_resources on 'Ringtone'
        m2m_table_name = db.shorten_name(u'mobile_products_ringtone_audio_resources')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ringtone', models.ForeignKey(orm[u'mobile_products.ringtone'], null=False)),
            ('audioresource', models.ForeignKey(orm[u'mobile_products.audioresource'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ringtone_id', 'audioresource_id'])

        # Adding M2M table for field video_resources on 'Ringtone'
        m2m_table_name = db.shorten_name(u'mobile_products_ringtone_video_resources')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ringtone', models.ForeignKey(orm[u'mobile_products.ringtone'], null=False)),
            ('videoresource', models.ForeignKey(orm[u'mobile_products.videoresource'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ringtone_id', 'videoresource_id'])

        # Adding M2M table for field usage_rights on 'Ringtone'
        m2m_table_name = db.shorten_name(u'mobile_products_ringtone_usage_rights')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ringtone', models.ForeignKey(orm[u'mobile_products.ringtone'], null=False)),
            ('usageright', models.ForeignKey(orm[u'mobile_products.usageright'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ringtone_id', 'usageright_id'])

        # Adding model 'MobileProduct'
        db.create_table(u'mobile_products_mobileproduct', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alternate_genre', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('alternate_subgenre', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('attachments', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mobile_products.Attachment'], null=True, blank=True)),
            ('catalog_tier', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('catalog_number', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
            ('consumer_release_date', self.gf('django.db.models.fields.DateField')()),
            ('cover_art', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mobile_products.CoverArt'], null=True, blank=True)),
            ('copyright_owner', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('copyright_year', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('display_artist', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('exclusive_for', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('fuga_delivery_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('main_genre', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('main_subgenre', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('original_release_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('parental_advisory', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('product_version', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('publishing_rights_owner', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('publishing_rights_year', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('recording_location', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('recording_year', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('total_play_time', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('upc_code', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'mobile_products', ['MobileProduct'])

        # Adding M2M table for field artists on 'MobileProduct'
        m2m_table_name = db.shorten_name(u'mobile_products_mobileproduct_artists')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mobileproduct', models.ForeignKey(orm[u'mobile_products.mobileproduct'], null=False)),
            ('artist', models.ForeignKey(orm[u'mobile_products.artist'], null=False))
        ))
        db.create_unique(m2m_table_name, ['mobileproduct_id', 'artist_id'])

        # Adding M2M table for field ringtones on 'MobileProduct'
        m2m_table_name = db.shorten_name(u'mobile_products_mobileproduct_ringtones')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mobileproduct', models.ForeignKey(orm[u'mobile_products.mobileproduct'], null=False)),
            ('ringtone', models.ForeignKey(orm[u'mobile_products.ringtone'], null=False))
        ))
        db.create_unique(m2m_table_name, ['mobileproduct_id', 'ringtone_id'])

        # Adding M2M table for field usage_rights on 'MobileProduct'
        m2m_table_name = db.shorten_name(u'mobile_products_mobileproduct_usage_rights')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mobileproduct', models.ForeignKey(orm[u'mobile_products.mobileproduct'], null=False)),
            ('usageright', models.ForeignKey(orm[u'mobile_products.usageright'], null=False))
        ))
        db.create_unique(m2m_table_name, ['mobileproduct_id', 'usageright_id'])


    def backwards(self, orm):
        # Deleting model 'Artist'
        db.delete_table(u'mobile_products_artist')

        # Deleting model 'AttachmentFile'
        db.delete_table(u'mobile_products_attachmentfile')

        # Deleting model 'Attachment'
        db.delete_table(u'mobile_products_attachment')

        # Deleting model 'CoverArt'
        db.delete_table(u'mobile_products_coverart')

        # Deleting model 'Contributor'
        db.delete_table(u'mobile_products_contributor')

        # Deleting model 'Publisher'
        db.delete_table(u'mobile_products_publisher')

        # Deleting model 'AudioResource'
        db.delete_table(u'mobile_products_audioresource')

        # Deleting model 'VideoResource'
        db.delete_table(u'mobile_products_videoresource')

        # Deleting model 'UsageRight'
        db.delete_table(u'mobile_products_usageright')

        # Deleting model 'Ringtone'
        db.delete_table(u'mobile_products_ringtone')

        # Removing M2M table for field artists on 'Ringtone'
        db.delete_table(db.shorten_name(u'mobile_products_ringtone_artists'))

        # Removing M2M table for field contributors on 'Ringtone'
        db.delete_table(db.shorten_name(u'mobile_products_ringtone_contributors'))

        # Removing M2M table for field publishers on 'Ringtone'
        db.delete_table(db.shorten_name(u'mobile_products_ringtone_publishers'))

        # Removing M2M table for field audio_resources on 'Ringtone'
        db.delete_table(db.shorten_name(u'mobile_products_ringtone_audio_resources'))

        # Removing M2M table for field video_resources on 'Ringtone'
        db.delete_table(db.shorten_name(u'mobile_products_ringtone_video_resources'))

        # Removing M2M table for field usage_rights on 'Ringtone'
        db.delete_table(db.shorten_name(u'mobile_products_ringtone_usage_rights'))

        # Deleting model 'MobileProduct'
        db.delete_table(u'mobile_products_mobileproduct')

        # Removing M2M table for field artists on 'MobileProduct'
        db.delete_table(db.shorten_name(u'mobile_products_mobileproduct_artists'))

        # Removing M2M table for field ringtones on 'MobileProduct'
        db.delete_table(db.shorten_name(u'mobile_products_mobileproduct_ringtones'))

        # Removing M2M table for field usage_rights on 'MobileProduct'
        db.delete_table(db.shorten_name(u'mobile_products_mobileproduct_usage_rights'))


    models = {
        u'mobile_products.artist': {
            'Meta': {'object_name': 'Artist'},
            'biography': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_primary': ('django.db.models.fields.BooleanField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'mobile_products.attachment': {
            'Meta': {'object_name': 'Attachment'},
            'attachment_file': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['mobile_products.AttachmentFile']", 'unique': 'True'}),
            'attachment_type': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'original_file_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'})
        },
        u'mobile_products.attachmentfile': {
            'Meta': {'object_name': 'AttachmentFile'},
            'crc32_checksum': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'size': ('django.db.models.fields.IntegerField', [], {})
        },
        u'mobile_products.audioresource': {
            'Meta': {'object_name': 'AudioResource'},
            'duration': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recording_type': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'resource_file': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mobile_products.AttachmentFile']"})
        },
        u'mobile_products.contributor': {
            'Meta': {'object_name': 'Contributor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'mobile_products.coverart': {
            'Meta': {'object_name': 'CoverArt'},
            'attachment_file': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['mobile_products.AttachmentFile']", 'unique': 'True'}),
            'color_model': ('django.db.models.fields.CharField', [], {'default': "'RGB'", 'max_length': '8'}),
            'file_format': ('django.db.models.fields.CharField', [], {'default': "'JPEG'", 'max_length': '8'}),
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'mobile_products.mobileproduct': {
            'Meta': {'object_name': 'MobileProduct'},
            'alternate_genre': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'alternate_subgenre': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'artists': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mobile_products.Artist']", 'symmetrical': 'False'}),
            'attachments': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mobile_products.Attachment']", 'null': 'True', 'blank': 'True'}),
            'catalog_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'catalog_tier': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'consumer_release_date': ('django.db.models.fields.DateField', [], {}),
            'copyright_owner': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'copyright_year': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'cover_art': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mobile_products.CoverArt']", 'null': 'True', 'blank': 'True'}),
            'display_artist': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'exclusive_for': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'fuga_delivery_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'main_genre': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'main_subgenre': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'original_release_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'parental_advisory': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'product_version': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'publishing_rights_owner': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'publishing_rights_year': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'recording_location': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'recording_year': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ringtones': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mobile_products.Ringtone']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'total_play_time': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'upc_code': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'usage_rights': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mobile_products.UsageRight']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'mobile_products.publisher': {
            'Meta': {'object_name': 'Publisher'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'writer': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'mobile_products.ringtone': {
            'Meta': {'object_name': 'Ringtone'},
            'alternate_genre': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'alternate_subgenre': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'artists': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mobile_products.Artist']", 'symmetrical': 'False'}),
            'audio_resources': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mobile_products.AudioResource']", 'symmetrical': 'False', 'blank': 'True'}),
            'available_separately': ('django.db.models.fields.BooleanField', [], {}),
            'catalog_tier': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'contributors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mobile_products.Contributor']", 'symmetrical': 'False'}),
            'country_of_commissioning': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'country_of_recording': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'display_artist': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'duration': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isrc_code': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'lyrics': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'main_genre': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'main_subgenre': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'parental_advisory': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'publishers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mobile_products.Publisher']", 'symmetrical': 'False'}),
            'publishing_rights_owner': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'publishing_rights_year': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'recording_location': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'recording_year': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rights_contract_begin_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'rights_holder_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'rights_ownership_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'sequence_number': ('django.db.models.fields.IntegerField', [], {}),
            'suggested_preview_length': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'suggested_preview_start': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'usage_rights': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mobile_products.UsageRight']", 'symmetrical': 'False', 'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'video_resources': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mobile_products.VideoResource']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'mobile_products.usageright': {
            'Meta': {'object_name': 'UsageRight'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'mobile_products.videoresource': {
            'Meta': {'object_name': 'VideoResource'},
            'bitrate': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'dimensions': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'encoding': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'file_format': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'fps': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resource_file': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mobile_products.AttachmentFile']"})
        }
    }

    complete_apps = ['mobile_products']