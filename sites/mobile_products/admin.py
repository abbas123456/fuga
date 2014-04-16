from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from mobile_products import models
from django.shortcuts import render_to_response
from django.template.loader import render_to_string


class MobileProductAdmin(SummernoteModelAdmin):
    
    class Media:
        js = (
            'js/admin.js',
        )
        
    list_display = ('title', 'main_genre', 'display_artist', 'catalog_tier',
                    'consumer_release_date', 'status', 'cover_art_image',
                    'status_button')

    fieldsets = [
                 ('Product overview', {'fields': ['title', 'upc_code',
                                                  'status', 'label',
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
                                         'recording_year',
                                         'total_play_time']}),
                 ('Media', {'fields': ['attachments', 'cover_art',
                                       'display_artist']}),
                 ('Rights', {'fields': ['copyright_owner', 'copyright_year',
                                        'publishing_rights_owner',
                                        'publishing_rights_year', ]}),
                 ]

    def cover_art_image(self, model):
        return render_to_string('partials/cover_art_image.html',
                                {'model': model})

    def status_button(self, model):
        return render_to_string('partials/status_button.html',
                                {'model': model})


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
