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
    name = models.CharField(max_length=128, blank=True)
    description = models.TextField(blank=True)
    attachment_type = models.CharField(max_length=16)
    original_file_name = models.CharField(max_length=128, blank=True)
    attachment_file = models.OneToOneField(AttachmentFile)


class CoverArt(models.Model):
    color_model = models.CharField(max_length=8, default="RGB")
    width = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    file_format = models.CharField(max_length=8, default="JPEG")
    attachment_file = models.OneToOneField(AttachmentFile)


class Contributor(models.Model):
    name = models.CharField(max_length=128)
    role = models.CharField(max_length=64)


class Publisher(models.Model):
    publisher = models.CharField(max_length=128)
    writer = models.CharField(max_length=128)


class AudioResource(models.Model):
    recording_type = models.CharField(max_length=16)
    duration = models.PositiveIntegerField(help_text=_("The total total "
                                                       "play time in "
                                                       "seconds"))
    resource_file = models.ForeignKey(AttachmentFile)


class VideoResource(models.Model):
    file_format = models.CharField(max_length=4)
    encoding = models.CharField(max_length=4)
    bitrate = models.PositiveIntegerField()
    dimensions = models.CharField(max_length=16)
    fps = models.PositiveIntegerField()
    resource_file = models.ForeignKey(AttachmentFile)


class Resources(models.Model):
    audio_resource = models.ForeignKey(AudioResource)
    video_resource = models.ForeignKey(VideoResource)


class UsageRight(models.Model):
    name = models.CharField(max_length=64)


class Ringtone(models.Model):
    alternate_genre = models.CharField(max_length=32, blank=True)
    alternate_subgenre = models.CharField(max_length=32, blank=True)
    artists = models.ForeignKey(Artist)
    available_seperately = models.BooleanField()
    catalogue_tier = models.CharField(max_length=64)
    contributors = models.ForeignKey(Contributor)
    country_of_commissioning = models.CharField(max_length=128, blank=True)
    country_of_recording = models.CharField(max_length=128, blank=True)
    display_artist = models.CharField(max_length=128)
    duration = models.PositiveIntegerField(help_text=_("The total total "
                                                       "play time in "
                                                       "seconds"))
    isrc_code = models.CharField(max_length=12)
    lyrics = models.TextField(blank=True)
    main_genre = models.CharField(max_length=32)
    main_subgenre = models.CharField(max_length=32, blank=True)
    notes = models.TextField(blank=True)
    parental_advisory = models.NullBooleanField()
    publishing_rights_owner = models.CharField(max_length=128, blank=True)
    publishing_rights_year = models.PositiveIntegerField(null=True, blank=True)
    publishers = models.ForeignKey(Publisher)
    recording_location = models.CharField(max_length=128, blank=True)
    recording_year = models.PositiveIntegerField(null=True, blank=True)
    resources = models.ForeignKey(Resources)
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
    usage_rights = models.ForeignKey(UsageRight)
    version = models.CharField(max_length=64, blank=True)


class MobileProduct(models.Model):
    alternate_genre = models.CharField(max_length=32, blank=True)
    alternate_subgenre = models.CharField(max_length=32, blank=True)
    attachments = models.ForeignKey(Attachment)
    artists = models.ForeignKey(Artist)
    catalogue_tier = models.CharField(max_length=64)
    catalog_number = models.CharField(max_length=32, unique=True)
    consumer_release_date = models.DateField()
    cover_art = models.ForeignKey(CoverArt)
    copyright_owner = models.CharField(max_length=128)
    copyright_year = models.PositiveIntegerField()
    display_artist = models.CharField(max_length=128)
    exclusive_for = models.PositiveIntegerField(_("Number of days for which "
                                                  "no party is allowed to "
                                                  "publish the product"))
    fuga_delivery_id = models.PositiveIntegerField()
    label = models.CharField(max_length=128)
    main_genre = models.CharField(max_length=32)
    main_subgenre = models.CharField(max_length=32, blank=True)
    original_release_date = models.DateField(null=True, blank=True)
    parental_advisory = models.NullBooleanField()
    product_version = models.CharField(max_length=128, blank=True)
    publishing_rights_owner = models.CharField(max_length=128)
    publishing_rights_year = models.PositiveIntegerField()
    recording_location = models.CharField(max_length=128, blank=True)
    recording_year = models.PositiveIntegerField(null=True, blank=True)
    ringtones = models.ForeignKey(Ringtone)
    total_play_time = models.PositiveIntegerField(help_text=_("The total total "
                                                              "play time in "
                                                              "seconds"))
    title = models.CharField(max_length=128)
    upc_code = models.CharField(max_length=32)
    usage_rights = models.ForeignKey(UsageRight)


