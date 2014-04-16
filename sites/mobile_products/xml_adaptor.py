from adaptor import model, fields
from mobile_products import models


def add_models_to_many_to_many_relationship(base_model, xml_models, relationship):
    for xml_model in xml_models:
        xml_model.create_model_instance(xml_model.as_dict())
        many_to_many_related_manager = getattr(base_model, relationship)
        many_to_many_related_manager.add(xml_model.object)


class ArtistModel(model.XMLModel):
    multiple_creation_field = False

    class Meta:
        dbModel = models.Artist
        update = {'keys': ['id', ]}

    root = fields.XMLRootField(path="artists/artist")
    id = fields.XMLIntegerField(path="id")
    biography = fields.XMLCharField(path="biography")
    is_primary = fields.XMLBooleanField(path="primary")
    name = fields.XMLCharField(path="name")


class AttachmentFileModel(model.XMLModel):
    multiple_creation_field = False

    class Meta:
        dbModel = models.AttachmentFile

    root = fields.XMLRootField(path="file")
    file_path = fields.XMLCharField(path="path")
    name = fields.XMLCharField(path="name")
    crc32_checksum = fields.XMLCharField(path="crc32_checksum")
    size = fields.XMLIntegerField(path="size")


class AttachmentModel(model.XMLModel):
    multiple_creation_field = False

    class Meta:
        dbModel = models.Attachment

    root = fields.XMLRootField(path="attachments/attachment")
    name = fields.XMLCharField(path="name", null=True)
    description = fields.XMLCharField(path="description", null=True)
    attachment_type = fields.XMLCharField(path="attachment_type")
    original_file_name = fields.XMLCharField(path="original_file_name",
                                             null=True)
    attachment_file = fields.XMLEmbed(AttachmentFileModel)

    def as_dict(self):
        """
        This method is used to create a clean dictionary of fields that are
        passed as kwargs to CoverArtModel.objects.create() by the Adaptor
        libary.
        """
        values = super(AttachmentModel, self).as_dict()
        xml_model = values['attachment_file'][0]
        xml_model.create_model_instance(xml_model.as_dict())
        values['attachment_file'] = xml_model.object
        return values


class CoverArtModel(model.XMLModel):
    multiple_creation_field = False

    class Meta:
        dbModel = models.CoverArt

    root = fields.XMLRootField(path="cover_art/image")
    color_model = fields.XMLCharField(path="color_model")
    width = fields.XMLIntegerField(path="width", null=True)
    height = fields.XMLIntegerField(path="height", null=True)
    file_format = fields.XMLCharField(path="file_format")
    attachment_file = fields.XMLEmbed(AttachmentFileModel)

    def as_dict(self):
        """
        This method is used to create a clean dictionary of fields that are
        passed as kwargs to CoverArtModel.objects.create() by the Adaptor
        libary.
        """
        values = super(CoverArtModel, self).as_dict()
        xml_model = values['attachment_file'][0]
        xml_model.create_model_instance(xml_model.as_dict())
        values['attachment_file'] = xml_model.object
        return values


class ContributorModel(model.XMLModel):
    multiple_creation_field = False

    class Meta:
        dbModel = models.Contributor

    root = fields.XMLRootField(path="contributors/contributor")
    name = fields.XMLCharField(path="name")
    role = fields.XMLCharField(path="role")


class PublisherModel(model.XMLModel):
    multiple_creation_field = False

    class Meta:
        dbModel = models.Publisher

    root = fields.XMLRootField(path="publishers/publisher")
    publisher = fields.XMLCharField(path="publisher_name")
    writer = fields.XMLCharField(path="writer_name")


class AudioResourceModel(model.XMLModel):
    multiple_creation_field = False

    class Meta:
        dbModel = models.AudioResource

    root = fields.XMLRootField(path="resources/audio")
    recording_type = fields.XMLCharField(path="recording_type")
    duration = fields.XMLIntegerField(path="duration")
    resource_file = fields.XMLEmbed(AttachmentFileModel)

    def as_dict(self):
        """
        This method is used to create a clean dictionary of fields that are
        passed as kwargs to AudioResourceModel.objects.create() by the Adaptor
        libary.
        """
        values = super(AudioResourceModel, self).as_dict()
        # Foreign key fields are treated as lists by the adaptor library
        # so the first item is taken and a model is created using it
        if values['resource_file']:
            xml_model = values['resource_file'][0]
            xml_model.create_model_instance(xml_model.as_dict())
            values['resource_file'] = xml_model.object
        else:
            values['resource_file'] = None
        return values


class VideoResourceModel(model.XMLModel):
    multiple_creation_field = False

    class Meta:
        dbModel = models.VideoResource

    root = fields.XMLRootField(path="resources/video")
    file_format = fields.XMLCharField(path="file_format")
    encoding = fields.XMLCharField(path="encoding")
    bitrate = fields.XMLIntegerField(path="bitrate")
    dimensions = fields.XMLCharField(path="dimensions")
    fps = fields.XMLIntegerField(path="fps")
    resource_file = fields.XMLEmbed(AttachmentFileModel)

    def as_dict(self):
        """
        This method is used to create a clean dictionary of fields that are
        passed as kwargs to VideoResourceModel.objects.create() by the Adaptor
        libary.
        """
        values = super(VideoResourceModel, self).as_dict()
        # Foreign key fields are treated as lists by the adaptor library
        # so the first item is taken and a model is created using it
        if values['resource_file']:
            xml_model = values['resource_file'][0]
            xml_model.create_model_instance(xml_model.as_dict())
            values['resource_file'] = xml_model.object
        else:
            values['resource_file'] = None
        return values


class UsageRightModel(model.XMLModel):
    multiple_creation_field = False

    class Meta:
        dbModel = models.UsageRight
        update = {'keys': ['name', ]}

    root = fields.XMLRootField(path="usage_rights/usage_right")
    name = fields.XMLCharField(path=".")


class RingtoneModel(model.XMLModel):
    multiple_creation_field = False

    class Meta:
        dbModel = models.Ringtone
        update = {'keys': ['id', ]}

    root = fields.XMLRootField(path="ringtones/ringtone")
    id = fields.XMLIntegerField(path="id")
    alternate_genre = fields.XMLCharField(path="alternate_genre", null=True)
    alternate_subgenre = fields.XMLCharField(path="alternate_subgenre",
                                             null=True)
    artists = fields.XMLEmbed(ArtistModel)
    available_separately = fields.XMLBooleanField(path="available_separately")
    catalog_tier = fields.XMLCharField(path="catalog_tier")
    contributors = fields.XMLEmbed(ContributorModel)
    country_of_commissioning = fields.XMLCharField(path="country_of_commissioning",
                                                   null=True)
    country_of_recording = fields.XMLCharField(path="country_of_recording",
                                               null=True)
    display_artist = fields.XMLCharField(path="display_artist")
    duration = fields.XMLIntegerField(path="duration")
    isrc_code = fields.XMLCharField(path="isrc_code")
    lyrics = fields.XMLCharField(path="lyrics", null=True)
    main_genre = fields.XMLCharField(path="main_genre")
    main_subgenre = fields.XMLCharField(path="main_subgenre", null=True)
    notes = fields.XMLCharField(path="ringtone_notes", null=True)
    parental_advisory = fields.XMLBooleanField(path="parental_advisory",
                                                null=True)
    publishing_rights_owner = fields.XMLCharField(path="p_line_text")
    publishing_rights_year = fields.XMLIntegerField(path="p_line_year")
    publishers = fields.XMLEmbed(PublisherModel)
    recording_location = fields.XMLCharField(path="recording_location",
                                             null=True)
    recording_year = fields.XMLIntegerField(path="recording_year", null=True)
    audio_resources = fields.XMLEmbed(AudioResourceModel)
    video_resources = fields.XMLEmbed(VideoResourceModel)
    rights_contract_begin_date = fields.XMLDateField(path="rights_contract_begin_date",
                                                     format="%Y-%m-%d",
                                                     null=True)
    rights_holder_name = fields.XMLCharField(path="rights_holder_name",
                                             null=True)
    rights_ownership_name = fields.XMLCharField(path="rights_ownership_name",
                                             null=True)
    sequence_number = fields.XMLIntegerField(path="sequence_number")

    suggested_preview_length = fields.XMLIntegerField(path="suggested_preview_length",
                                                      null=True)
    suggested_preview_start = fields.XMLIntegerField(path="suggested_preview_start",
                                                     null=True)
    title = fields.XMLCharField(path="name")
    usage_rights = fields.XMLEmbed(UsageRightModel)
    version = fields.XMLCharField(path="version", null=True)

    def create_model_instance(self, values):
        """
        This method is called by the add_models_to_many_to_many_relationship
        method which is called by the create_model_instance method of
        of the MobileProductModel class. It creates the Ringtone model in the
        database and then adds the appropriate many to many relationships
        """
        super(RingtoneModel, self).create_model_instance(values)
        add_models_to_many_to_many_relationship(self.object, self.usage_rights,
                                                "usage_rights")
        add_models_to_many_to_many_relationship(self.object, self.publishers,
                                                "publishers")
        add_models_to_many_to_many_relationship(self.object, self.artists,
                                                "artists")
        add_models_to_many_to_many_relationship(self.object,
                                                self.audio_resources,
                                                "audio_resources")
        add_models_to_many_to_many_relationship(self.object,
                                                self.video_resources,
                                                "video_resources")

    def as_dict(self):
        """
        This method is used to create a clean dictionary of fields that are
        passed as kwargs to Ringtone.objects.create() by the Adaptor
        libary. The important thing to note is that many to many fields are
        stripped out as Django does not accept these as kwargs when creating
        a model.
        """
        values = super(RingtoneModel, self).as_dict()
        # Many to many fields need to be created later
        del(values['usage_rights'])
        del(values['publishers'])
        del(values['artists'])
        del(values['contributors'])
        del(values['audio_resources'])
        del(values['video_resources'])
        return values


class MobileProductModel(model.XMLModel):
    multiple_creation_field = False

    class Meta:
        dbModel = models.MobileProduct
        update = {'keys': ['id', ]}

    root = fields.XMLRootField(path="/mobile_product")
    id = fields.XMLIntegerField(path="id")
    alternate_genre = fields.XMLCharField(path="alternate_genre", null=True)
    alternate_subgenre = fields.XMLCharField(path="alternate_subgenre",
                                             null=True)
    artists = fields.XMLEmbed(ArtistModel)
    attachments = fields.XMLEmbed(AttachmentModel)
    catalog_tier = fields.XMLCharField(path="catalog_tier")
    catalog_number = fields.XMLCharField(path="catalog_number")
    consumer_release_date = fields.XMLDateField(path="consumer_release_date",
                                                format="%Y-%m-%d")
    cover_art = fields.XMLEmbed(CoverArtModel)
    copyright_owner = fields.XMLCharField(path="c_line_text")
    copyright_year = fields.XMLIntegerField(path="c_line_year")
    display_artist = fields.XMLCharField(path="display_artist")
    exclusive_for = fields.XMLIntegerField(path="exclusive_for")
    fuga_delivery_id = fields.XMLIntegerField(path="fuga_delivery_id")
    label = fields.XMLCharField(path="label")
    main_genre = fields.XMLCharField(path="main_genre")
    main_subgenre = fields.XMLCharField(path="main_subgenre", null=True)
    notes = fields.XMLCharField(path="mobile_product_notes", null=True)
    original_release_date = fields.XMLDateField(path="original_release_date",
                                             format="%Y-%m-%d", null=True)
    parental_advisory = fields.XMLBooleanField(path="parental_advisory",
                                                null=True)
    product_version = fields.XMLCharField(path="product_version", null=True)
    publishing_rights_owner = fields.XMLCharField(path="p_line_text")
    publishing_rights_year = fields.XMLIntegerField(path="p_line_year")
    recording_location = fields.XMLCharField(path="recording_location",
                                             null=True)
    recording_year = fields.XMLIntegerField(path="recording_year", null=True)
    ringtones = fields.XMLEmbed(RingtoneModel)
    total_play_time = fields.XMLIntegerField(path="total_play_time")
    title = fields.XMLCharField(path="name")
    upc_code = fields.XMLCharField(path="upc_code")
    usage_rights = fields.XMLEmbed(UsageRightModel)

    def create_model_instance(self, values):
        """
        This method is called by the add_models_to_many_to_many_relationship
        method which is called by the create_model_instance method of
        of the MobileProductModel class. It creates the Ringtone model in the
        database and then adds the appropriate many to many relationships
        """
        super(MobileProductModel, self).create_model_instance(values)
        add_models_to_many_to_many_relationship(self.object, self.usage_rights,
                                                "usage_rights")
        add_models_to_many_to_many_relationship(self.object, self.ringtones,
                                                "ringtones")
        add_models_to_many_to_many_relationship(self.object, self.artists,
                                                "artists")

    def as_dict(self):
        """
        This method is used to create a clean dictionary of fields that are
        passed as kwargs to MobileProduct.objects.create() by the Adaptor
        libary. The important thing to note is that many to many fields are
        stripped out as Django does not accept these as kwargs when creating
        a model.
        """
        values = super(MobileProductModel, self).as_dict()
        # Foreign key fields are treated as lists by the adaptor library
        # so the first item is taken and a model is created using it
        if values['attachments']:
            xml_model = values['attachments'][0]
            xml_model.create_model_instance(xml_model.as_dict())
            values['attachments'] = xml_model.object
        else:
            values['attachments'] = None

        if values['cover_art']:
            xml_model = values['cover_art'][0]
            xml_model.create_model_instance(xml_model.as_dict())
            values['cover_art'] = xml_model.object
        else:
            values['cover_art'] = None

        # Many to many fields need to be created later
        del(values['usage_rights'])
        del(values['ringtones'])
        del(values['artists'])

        return values
