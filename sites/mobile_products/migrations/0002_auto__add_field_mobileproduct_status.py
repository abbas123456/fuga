# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MobileProduct.status'
        db.add_column(u'mobile_products_mobileproduct', 'status',
                      self.gf('django.db.models.fields.CharField')(default='Draft', max_length=16),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MobileProduct.status'
        db.delete_column(u'mobile_products_mobileproduct', 'status')


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
            'attachment_file': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mobile_products.AttachmentFile']"}),
            'attachment_type': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'original_file_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        },
        u'mobile_products.attachmentfile': {
            'Meta': {'object_name': 'AttachmentFile'},
            'crc32_checksum': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'file_path': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
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
            'attachment_file': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mobile_products.AttachmentFile']"}),
            'color_model': ('django.db.models.fields.CharField', [], {'default': "'RGB'", 'max_length': '8'}),
            'file_format': ('django.db.models.fields.CharField', [], {'default': "'JPEG'", 'max_length': '8'}),
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'mobile_products.mobileproduct': {
            'Meta': {'object_name': 'MobileProduct'},
            'alternate_genre': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'alternate_subgenre': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
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
            'main_subgenre': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'original_release_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'parental_advisory': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'product_version': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'publishing_rights_owner': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'publishing_rights_year': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'recording_location': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'recording_year': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ringtones': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mobile_products.Ringtone']", 'symmetrical': 'False'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Draft'", 'max_length': '16'}),
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
            'alternate_genre': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'alternate_subgenre': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'artists': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mobile_products.Artist']", 'symmetrical': 'False'}),
            'audio_resources': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mobile_products.AudioResource']", 'symmetrical': 'False', 'blank': 'True'}),
            'available_separately': ('django.db.models.fields.BooleanField', [], {}),
            'catalog_tier': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'contributors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mobile_products.Contributor']", 'symmetrical': 'False'}),
            'country_of_commissioning': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'country_of_recording': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'display_artist': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'duration': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isrc_code': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'lyrics': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'main_genre': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'main_subgenre': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'parental_advisory': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'publishers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mobile_products.Publisher']", 'symmetrical': 'False'}),
            'publishing_rights_owner': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'publishing_rights_year': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'recording_location': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'recording_year': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rights_contract_begin_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'rights_holder_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'rights_ownership_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'sequence_number': ('django.db.models.fields.IntegerField', [], {}),
            'suggested_preview_length': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'suggested_preview_start': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'usage_rights': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mobile_products.UsageRight']", 'symmetrical': 'False', 'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
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