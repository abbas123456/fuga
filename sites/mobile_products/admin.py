from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from mobile_products import models


class MobileProductAdmin(SummernoteModelAdmin):
    list_display = ('title', 'main_genre', 'display_artist', 'catalog_tier',
                    'consumer_release_date', 'status')

    fieldsets = [
                 ('Product overview', {'fields': ['title', 'upc_code', 'status',
                                                  'label',
                                    'artists', 'ringtones', 'usage_rights']}),
                 ('Dates', {'fields': ['consumer_release_date',
                                       'original_release_date']}),
                 ('Genre', {'fields': ['main_genre', 'main_subgenre',
                                       'alternate_genre',
                                       'alternate_subgenre']}),
                 ('Catalog', {'fields': ['catalog_number', 'catalog_tier',
                                         'fuga_delivery_id']}),
                 ('Details', {'fields': ['exclusive_for', 'notes',
                                         'parental_advisory',
                                         'product_version',
                                         'recording_location',
                                         'recording_year', 'total_play_time']}),
                 ('Media', {'fields': ['attachments', 'cover_art',
                                       'display_artist']}),
                 ('Rights', {'fields': ['copyright_owner', 'copyright_year',
                                        'publishing_rights_owner',
                                        'publishing_rights_year', ]}),
                 ]

admin.site.register(models.Artist, SummernoteModelAdmin)
admin.site.register(models.Attachment, SummernoteModelAdmin)
admin.site.register(models.AttachmentFile, SummernoteModelAdmin)
admin.site.register(models.AudioResource, SummernoteModelAdmin)
admin.site.register(models.Contributor, SummernoteModelAdmin)
admin.site.register(models.CoverArt, SummernoteModelAdmin)
admin.site.register(models.MobileProduct, MobileProductAdmin)
admin.site.register(models.Publisher, SummernoteModelAdmin)
admin.site.register(models.Ringtone, SummernoteModelAdmin)
admin.site.register(models.UsageRight, SummernoteModelAdmin)
admin.site.register(models.VideoResource, SummernoteModelAdmin)