from django.db import models
from django.utils.translation import ugettext_lazy as _


class Artist(models.Model):
    biography = models.TextField()
    is_primary = models.BooleanField()
    name = models.CharField(max_length=128)


class AttachmentFile(models.Model):
    path = models.CharField(max_length=256)
    name = models.CharField(max_length=128)
    crc32_checksum = models.CharField(max_length=32)
    size = models.IntegerField()


class Attachment(models.Model):
    ATTACHMENT_TYPE_CHOICES = (('REGULAR', 'REGULAR'),
                               ('BOOKLET', 'BOOKLET'))

    name = models.CharField(max_length=128, blank=True)
    description = models.TextField(blank=True)
    attachment_type = models.CharField(max_length=16,
                                       choices=ATTACHMENT_TYPE_CHOICES)
    original_file_name = models.CharField(max_length=128, blank=True)
    attachment_file = models.OneToOneField(AttachmentFile)


class CoverArt(models.Model):
    COLOR_MODEL_CHOICES = (('RGB', 'RGB'),
                           ('CMYK', 'CMYK'))
    FILE_FORMAT_CHOICES = (('JPEG', 'JPEG'),
                            ('PNG', 'PNG'),
                            ('GIF', 'GIF'),
                            ('TIFF', 'TIFF'),
                            ('BMP', 'BMP'))

    color_model = models.CharField(max_length=8, choices=COLOR_MODEL_CHOICES,
                                   default="RGB")
    width = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    file_format = models.CharField(max_length=8, choices=FILE_FORMAT_CHOICES,
                                   default="JPEG")
    attachment_file = models.OneToOneField(AttachmentFile)


class Contributor(models.Model):
    ROLE_CHOICES = (('Arranger', 'Arranger'),
                    ('Choir', 'Choir'),
                    ('Composer', 'Composer'),
                    ('Conductor', 'Conductor'),
                    ('Contributing Artist', 'Contributing Artist'),
                    ('Engineer', 'Engineer'),
                    ('Ensemble', 'Ensemble'),
                    ('Featuring', 'Featuring'),
                    ('Lyricist', 'Lyricist'),
                    ('Mixer', 'Mixer'),
                    ('Orchestra', 'Orchestra'),
                    ('Performer', 'Performer'),
                    ('Producer', 'Producer'),
                    ('Remixer', 'Remixer'),
                    ('Soloist', 'Soloist'),
                    ('Writer', 'Writer'))

    name = models.CharField(max_length=128)
    role = models.CharField(max_length=64, choices=ROLE_CHOICES)


class Publisher(models.Model):
    publisher = models.CharField(max_length=128)
    writer = models.CharField(max_length=128)


class AudioResource(models.Model):
    RECORDING_TYPE_CHOICES = (('full', 'full'),
                              ('preview', 'preview'))

    recording_type = models.CharField(max_length=16,
                                      choices=RECORDING_TYPE_CHOICES)
    duration = models.PositiveIntegerField(help_text=_("The total "
                                                       "play time in "
                                                       "seconds"))
    resource_file = models.ForeignKey(AttachmentFile)


class VideoResource(models.Model):
    FILE_FORMAT_CHOICES = (('M4V', 'M4V'),)
    ENCODING_CHOICES = (('H264', 'H264'),)
    BITRATE_CHOICES = ((300, 300),
                       (500, 500),
                       (800, 800),
                       (1500, 1500),
                       (6000, 6000))
    DIMENSIONS_CHOICES = (('320x240', '320x240'),
                          ('640x480', '640x480'),
                          ('720x576', '720x576'),
                          ('1280x720', '1280x720'),
                          ('1920x1080', '1920x1080'))
    FPS_CHOICES = ((25, 25),)

    file_format = models.CharField(max_length=4, choices=FILE_FORMAT_CHOICES)
    encoding = models.CharField(max_length=4, choices=ENCODING_CHOICES)
    bitrate = models.PositiveIntegerField(choices=BITRATE_CHOICES)
    dimensions = models.CharField(max_length=16, choices=DIMENSIONS_CHOICES)
    fps = models.PositiveIntegerField(choices=FPS_CHOICES)
    resource_file = models.ForeignKey(AttachmentFile)


class UsageRight(models.Model):
    NAME_CHOICES = (('SubscriptionStreaming', 'SubscriptionStreaming'),
                    ('AdSupportedStreaming', 'AdSupportedStreaming'),
                    ('SubscriptionDownload', 'SubscriptionDownload'),
                    ('PermanentDownload', 'PermanentDownload'),
                    ('UserGeneratedAudio', 'UserGeneratedAudio'),
                    ('UserGeneratedVideo', 'UserGeneratedVideo'),
                    ('UserGeneratedRingtone', 'UserGeneratedRingtone'),
                    ('BurnCD', 'BurnCD'))

    name = models.CharField(max_length=64, choices=NAME_CHOICES)


GENRE_CHOICES = (('Alternative', 'Alternative'),
                 ('Audiobooks', 'Audiobooks'),
                 ('Blues', 'Blues'),
                 ('Children''s Music', 'Children''s Music'),
                 ('Classical', 'Classical'),
                 ('Comedy', 'Comedy'),
                 ('Country', 'Country'),
                 ('Dance', 'Dance'),
                 ('Electronic', 'Electronic'),
                 ('Folk', 'Electronic'),
                 ('Hip Hop/Rap', 'Hip Hop/Rap'),
                 ('Holiday', 'Holiday'),
                 ('Inspirational', 'Inspirational'),
                 ('Jazz', 'Jazz'),
                 ('Latin', 'Latin'),
                 ('New Age', 'New Age'),
                 ('Opera', 'Opera'),
                 ('Pop', 'Pop'),
                 ('Rock', 'Rock'),
                 ('R&B/Soul', 'R&B/Soul'),
                 ('Reggae', 'Reggae'),
                 ('Soundtrack', 'Soundtrack'),
                 ('Spoken Word', 'Spoken Word'),
                 ('Vocal', 'Vocal'),
                 ('World', 'World'))


class Ringtone(models.Model):
    CATALOG_TIER_CHOICES = (('Front catalog', 'Front catalog'),
                        ('Mid catalog', 'Mid catalog'),
                        ('Back catalog', 'Back catalog'),
                        ('Free catalog', 'Free catalog'))

    alternate_genre = models.CharField(max_length=32, blank=True,
                                       choices=GENRE_CHOICES)
    alternate_subgenre = models.CharField(max_length=32, blank=True)
    artists = models.ManyToManyField(Artist)
    available_separately = models.BooleanField()
    catalog_tier = models.CharField(max_length=64,
                                    choices=CATALOG_TIER_CHOICES)
    contributors = models.ManyToManyField(Contributor)
    country_of_commissioning = models.CharField(max_length=128, blank=True)
    country_of_recording = models.CharField(max_length=128, blank=True)
    display_artist = models.CharField(max_length=128)
    duration = models.PositiveIntegerField(help_text=_("The total "
                                                       "play time in "
                                                       "seconds"))
    isrc_code = models.CharField(max_length=12)
    lyrics = models.TextField(blank=True)
    main_genre = models.CharField(max_length=32, choices=GENRE_CHOICES)
    main_subgenre = models.CharField(max_length=32, blank=True)
    notes = models.TextField(blank=True)
    parental_advisory = models.NullBooleanField()
    publishing_rights_owner = models.CharField(max_length=128, blank=True)
    publishing_rights_year = models.PositiveIntegerField(null=True, blank=True)
    publishers = models.ManyToManyField(Publisher)
    recording_location = models.CharField(max_length=128, blank=True)
    recording_year = models.PositiveIntegerField(null=True, blank=True)
    audio_resources = models.ManyToManyField(AudioResource,  blank=True)
    video_resources = models.ManyToManyField(VideoResource, blank=True)
    rights_contract_begin_date = models.DateField(null=True, blank=True)
    rights_holder_name = models.CharField(max_length=128, blank=True)
    sequence_number = models.IntegerField()

    suggested_preview_length = models.PositiveIntegerField(null=True,
                                                           blank=True,
                                                           help_text=_("In "
                                                                       "seconds"))
    suggested_preview_start = models.PositiveIntegerField(null=True,
                                                          blank=True,
                                                          help_text=_("In "
                                                                      "seconds"))
    title = models.CharField(max_length=128)
    usage_rights = models.ManyToManyField(UsageRight, blank=True)
    version = models.CharField(max_length=64, blank=True)


class MobileProduct(models.Model):
    CATALOG_TIER_CHOICES = (('Front catalog', 'Front catalog'),
                            ('Mid catalog', 'Mid catalog'),
                            ('Back catalog', 'Back catalog'),
                            ('Budget catalog', 'Budget catalog'),
                            ('Premium catalog', 'Premium catalog'))

    alternate_genre = models.CharField(max_length=32, blank=True,
                                       choices=GENRE_CHOICES)
    alternate_subgenre = models.CharField(max_length=32, blank=True)
    attachments = models.ForeignKey(Attachment, null=True, blank=True)
    artists = models.ManyToManyField(Artist)
    catalog_tier = models.CharField(max_length=64,
                                    choices=CATALOG_TIER_CHOICES)
    catalog_number = models.CharField(max_length=32, unique=True)
    consumer_release_date = models.DateField()
    cover_art = models.ForeignKey(CoverArt, null=True, blank=True)
    copyright_owner = models.CharField(max_length=128)
    copyright_year = models.PositiveIntegerField()
    display_artist = models.CharField(max_length=128)
    exclusive_for = models.PositiveIntegerField(_("Number of days for which "
                                                  "no party is allowed to "
                                                  "publish the product"))
    fuga_delivery_id = models.PositiveIntegerField()
    label = models.CharField(max_length=128)
    main_genre = models.CharField(max_length=32, choices=GENRE_CHOICES)
    main_subgenre = models.CharField(max_length=32, blank=True)
    notes = models.TextField(blank=True)
    original_release_date = models.DateField(null=True, blank=True)
    parental_advisory = models.NullBooleanField()
    product_version = models.CharField(max_length=128, blank=True)
    publishing_rights_owner = models.CharField(max_length=128)
    publishing_rights_year = models.PositiveIntegerField()
    recording_location = models.CharField(max_length=128, blank=True)
    recording_year = models.PositiveIntegerField(null=True, blank=True)
    ringtones = models.ManyToManyField(Ringtone)
    total_play_time = models.PositiveIntegerField(help_text=_("The total "
                                                              "play time in "
                                                              "seconds"))
    title = models.CharField(max_length=128)
    upc_code = models.CharField(max_length=32)
    usage_rights = models.ManyToManyField(UsageRight, blank=True)
