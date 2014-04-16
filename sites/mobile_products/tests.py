from django.test import TestCase
from django.core.management import call_command
from mobile_products.xml_adaptor import MobileProductModel
from mobile_products import models
from django.core.management.base import CommandError


class TestXmlAdaptorConversion(TestCase):

    xml_filename = "mobile_products/integration/example.xml"

    def setUp(self):
        xml_file_data = open(self.xml_filename).read()
        self.model = MobileProductModel.import_data(data=xml_file_data)[0]

    def test_assigns_correct_values_for_simple_fields(self):
        self.assertEqual(self.model.id, 22077)
        self.assertEqual(self.model.notes, "Music by: Heath Whitelock\n"
                                           "http://www.heathwhitelock.com/")
        self.assertEqual(self.model.catalog_number, "Rlabel000107")
        self.assertEqual(self.model.catalog_tier, "Front catalog")
        self.assertEqual(self.model.consumer_release_date.strftime("%Y-%m-%d"),
                         "2009-10-16")
        self.assertEqual(self.model.copyright_owner, "Copyright")
        self.assertEqual(self.model.copyright_year, 1958)
        self.assertEqual(self.model.display_artist, "Cypress Hill")
        self.assertEqual(self.model.exclusive_for, 0)
        self.assertEqual(self.model.fuga_delivery_id, 22080)
        self.assertEqual(self.model.label, "Columbia")
        self.assertEqual(self.model.main_genre, "Hip Hop/Rap")
        self.assertEqual(self.model.original_release_date.strftime("%Y-%m-%d"),
                         "1958-11-21")
        self.assertEqual(self.model.parental_advisory, False)
        self.assertEqual(self.model.publishing_rights_owner, "Copyright")
        self.assertEqual(self.model.publishing_rights_year, 1958)
        self.assertEqual(self.model.recording_location,
                         "Palm Springs, California")
        self.assertEqual(self.model.recording_year, 2004)
        self.assertEqual(self.model.total_play_time, 1210)
        self.assertEqual(self.model.title, "Black Sunday (ringtones)")
        self.assertEqual(self.model.upc_code, "8234567890626")
        self.assertEqual(len(self.model.usage_rights), 8)
        self.assertEqual(self.model.usage_rights[0].name,
                         "SubscriptionStreaming")

    def test_assigns_correct_number_of_artists(self):
        self.assertEqual(len(self.model.artists), 1)

    def test_assigns_correct_values_for_artists(self):
        self.assertEqual(len(self.model.artists), 1)
        expected_biography = ("After the Cypress Hill first album was crowned "
                             "the greatest boogie record of all time by rockers "
                             "worldwide, no one knew just how the hell they "
                             "could top it. But what were they thinking? "
                             "The dream boys always bring da neck-licking, "
                             "boot-scooting, soul-scratching, ass-shaking party " 
                             "tunes that never disappoint.")
        self.assertEqual(self.model.artists[0].biography, expected_biography)
        self.assertEqual(self.model.artists[0].id, 4769)
        self.assertEqual(self.model.artists[0].name, "Cypress Hill")
        self.assertTrue(self.model.artists[0].is_primary)

    def test_assigns_correct_values_for_cover_art(self):
        cover_art = self.model.cover_art[0]
        cover_art_attachment_file = cover_art.attachment_file[0]

        self.assertEqual(cover_art.color_model, "RGB")
        self.assertEqual(cover_art.file_format, "JPEG")
        self.assertEqual(cover_art_attachment_file.file_path,
                         "/fuga_test_provider/22080-8234567890626")
        self.assertEqual(cover_art_attachment_file.name,
                         "8234567890626.jpg")
        self.assertEqual(cover_art_attachment_file.crc32_checksum,
                         "1450072837")
        self.assertEqual(cover_art_attachment_file.size, 375039)

    def test_assigns_correct_number_of_ringones(self):
        self.assertEqual(len(self.model.ringtones), 5)

    def test_assigns_correct_values_for_ringtone(self):
        ringtone = self.model.ringtones[0]
        ringtone_audio_resource = ringtone.audio_resources[0]
        ringtone_audio_resource_file = ringtone_audio_resource.resource_file[0]

        self.assertEqual(ringtone.id, 6095)
        self.assertEqual(ringtone.main_genre, "Hip Hop/Rap")
        self.assertEqual(ringtone.available_separately, False)
        self.assertEqual(ringtone.catalog_tier, "Front catalog")
        self.assertEqual(ringtone.country_of_commissioning, "USA")
        self.assertEqual(ringtone.country_of_recording, "USA")
        self.assertEqual(ringtone.display_artist, "Cypress Hill")
        self.assertEqual(ringtone.duration, 242)
        self.assertEqual(ringtone_audio_resource.recording_type, "full")
        self.assertEqual(ringtone_audio_resource.duration, 242)
        self.assertEqual(ringtone_audio_resource_file.file_path,
                         "/fuga_test_provider/22080-8234567890626")
        self.assertEqual(ringtone_audio_resource_file.name,
                         "8234567890626_1_01_mp3_cbr_128.mp3")
        self.assertEqual(ringtone_audio_resource_file.crc32_checksum,
                         "1267345975")
        self.assertEqual(ringtone_audio_resource_file.size, 3889280)
        self.assertEqual(ringtone.isrc_code, "LABEL0000241")
        self.assertEqual(ringtone.lyrics, None)

        self.assertEqual(ringtone.title, "I Wanna Get High")
        self.assertEqual(ringtone.publishing_rights_owner, "Copyright")
        self.assertEqual(ringtone.publishing_rights_year, 2009)
        self.assertFalse(ringtone.parental_advisory)
        self.assertEqual(ringtone.suggested_preview_length, 30)
        self.assertEqual(ringtone.suggested_preview_start, 10)
        self.assertEqual(len(ringtone.publishers), 0)
        self.assertEqual(ringtone.recording_year, 2004)
        self.assertEqual(ringtone.recording_location,
                         "Palm Springs, California")
        self.assertEqual(ringtone.sequence_number, 1)
        self.assertEqual(ringtone.rights_contract_begin_date.strftime("%Y-%m-%d"),
                         "1998-11-21")
        self.assertEqual(ringtone.rights_holder_name, "Cortez Records")
        self.assertEqual(ringtone.rights_ownership_name, "Cortez Records")
        self.assertEqual(ringtone.notes, "think about this")
        self.assertEqual(ringtone.version, None)
        self.assertEqual(len(ringtone.usage_rights), 8)
        self.assertEqual(ringtone.usage_rights[0].name,
                         "SubscriptionStreaming")

    def test_assigns_correct_values_for_ringtone_artists(self):
        ringtone = self.model.ringtones[0]
        self.assertEqual(len(ringtone.artists), 1)
        expected_biography = ("After the Cypress Hill first album was crowned "
                             "the greatest boogie record of all time by rockers "
                             "worldwide, no one knew just how the hell they "
                             "could top it. But what were they thinking? "
                             "The dream boys always bring da neck-licking, "
                             "boot-scooting, soul-scratching, ass-shaking party " 
                             "tunes that never disappoint.")
        self.assertEqual(ringtone.artists[0].biography, expected_biography)
        self.assertEqual(ringtone.artists[0].id, 4769)
        self.assertEqual(ringtone.artists[0].name, "Cypress Hill")
        self.assertTrue(ringtone.artists[0].is_primary)


class TestXmlAdaptorSave(TestCase):

    xml_filename = "mobile_products/integration/example.xml"

    def setUp(self):
        xml_file_data = open(self.xml_filename).read()
        model = MobileProductModel.import_data(data=xml_file_data)[0]
        model.create_model_instance(model.as_dict())

    def tearDown(self):
        models.MobileProduct.objects.all().delete()

    def test_creates_all_models_successfully(self):
        self.assertEqual(len(models.MobileProduct.objects.all()), 1)
        self.assertEqual(len(models.Ringtone.objects.all()), 5)
        self.assertEqual(len(models.Artist.objects.all()), 1)
        self.assertEqual(len(models.UsageRight.objects.all()), 8)

    def test_assigns_correct_values_for_mobile_product(self):
        mobile_product = models.MobileProduct.objects.all()[0]
        self.assertEqual(mobile_product.id, 22077)
        self.assertEqual(mobile_product.notes, "Music by: Heath Whitelock\n"
                                           "http://www.heathwhitelock.com/")
        self.assertEqual(mobile_product.catalog_number, "Rlabel000107")
        self.assertEqual(mobile_product.catalog_tier, "Front catalog")
        self.assertEqual(mobile_product.consumer_release_date.strftime("%Y-%m-%d"),
                         "2009-10-16")
        self.assertEqual(mobile_product.copyright_owner, "Copyright")
        self.assertEqual(mobile_product.copyright_year, 1958)
        self.assertEqual(mobile_product.display_artist, "Cypress Hill")
        self.assertEqual(mobile_product.exclusive_for, 0)
        self.assertEqual(mobile_product.fuga_delivery_id, 22080)
        self.assertEqual(mobile_product.label, "Columbia")
        self.assertEqual(mobile_product.main_genre, "Hip Hop/Rap")
        self.assertEqual(mobile_product.original_release_date.strftime("%Y-%m-%d"),
                         "1958-11-21")
        self.assertEqual(mobile_product.parental_advisory, False)
        self.assertEqual(mobile_product.publishing_rights_owner, "Copyright")
        self.assertEqual(mobile_product.publishing_rights_year, 1958)
        self.assertEqual(mobile_product.recording_location,
                         "Palm Springs, California")
        self.assertEqual(mobile_product.recording_year, 2004)
        self.assertEqual(mobile_product.total_play_time, 1210)
        self.assertEqual(mobile_product.title, "Black Sunday (ringtones)")
        self.assertEqual(mobile_product.upc_code, "8234567890626")
        self.assertEqual(mobile_product.cover_art.color_model, "RGB")
        self.assertEqual(mobile_product.cover_art.file_format, "JPEG")
        self.assertEqual(mobile_product.cover_art.attachment_file.file_path,
                         "/fuga_test_provider/22080-8234567890626")
        self.assertEqual(mobile_product.cover_art.attachment_file.name,
                         "8234567890626.jpg")
        self.assertEqual(mobile_product.cover_art.attachment_file.crc32_checksum,
                         "1450072837")
        self.assertEqual(mobile_product.cover_art.attachment_file.size, 375039)

    def test_sets_up_mobile_product_many_to_many_field(self):
        mobile_product = models.MobileProduct.objects.all()[0]
        self.assertEqual(len(mobile_product.usage_rights.all()), 8)
        self.assertEqual(len(mobile_product.ringtones.all()), 5)
        self.assertEqual(len(mobile_product.artists.all()), 1)

    def test_assigns_correct_values_for_ringtone(self):
        ringtone = models.MobileProduct.objects.all()[0].ringtones.all()[0]
        self.assertEqual(ringtone.id, 6095)
        self.assertEqual(ringtone.main_genre, "Hip Hop/Rap")
        self.assertEqual(ringtone.available_separately, False)
        self.assertEqual(ringtone.catalog_tier, "Front catalog")
        self.assertEqual(ringtone.country_of_commissioning, "USA")
        self.assertEqual(ringtone.country_of_recording, "USA")
        self.assertEqual(ringtone.display_artist, "Cypress Hill")
        self.assertEqual(ringtone.duration, 242)
        self.assertEqual(ringtone.audio_resources.all()[0].recording_type,
                         "full")
        self.assertEqual(ringtone.audio_resources.all()[0].duration, 242)
        self.assertEqual(ringtone.audio_resources.all()[0].resource_file.file_path,
                         "/fuga_test_provider/22080-8234567890626")
        self.assertEqual(ringtone.audio_resources.all()[0].resource_file.name,
                         "8234567890626_1_01_mp3_cbr_128.mp3")
        self.assertEqual(ringtone.audio_resources.all()[0].resource_file.crc32_checksum,
                         "1267345975")
        self.assertEqual(ringtone.audio_resources.all()[0].resource_file.size,
                         3889280)
        self.assertEqual(ringtone.isrc_code, "LABEL0000241")
        self.assertEqual(ringtone.lyrics, None)

        self.assertEqual(ringtone.title, "I Wanna Get High")
        self.assertEqual(ringtone.publishing_rights_owner, "Copyright")
        self.assertEqual(ringtone.publishing_rights_year, 2009)
        self.assertFalse(ringtone.parental_advisory)
        self.assertEqual(ringtone.suggested_preview_length, 30)
        self.assertEqual(ringtone.suggested_preview_start, 10)
        self.assertEqual(len(ringtone.publishers.all()), 0)
        self.assertEqual(ringtone.recording_year, 2004)
        self.assertEqual(ringtone.recording_location,
                         "Palm Springs, California")
        self.assertEqual(ringtone.sequence_number, 1)
        self.assertEqual(ringtone.rights_contract_begin_date.strftime("%Y-%m-%d"),
                         "1998-11-21")
        self.assertEqual(ringtone.rights_holder_name, "Cortez Records")
        self.assertEqual(ringtone.rights_ownership_name, "Cortez Records")
        self.assertEqual(ringtone.notes, "think about this")
        self.assertEqual(ringtone.version, None)
        self.assertEqual(len(ringtone.usage_rights.all()), 8)

    def test_assigns_correct_values_for_artists(self):
        artist = models.MobileProduct.objects.all()[0].artists.all()[0]
        expected_biography = ("After the Cypress Hill first album was crowned "
                             "the greatest boogie record of all time by rockers "
                             "worldwide, no one knew just how the hell they "
                             "could top it. But what were they thinking? "
                             "The dream boys always bring da neck-licking, "
                             "boot-scooting, soul-scratching, ass-shaking party " 
                             "tunes that never disappoint.")
        self.assertEqual(artist.biography, expected_biography)
        self.assertEqual(artist.id, 4769)
        self.assertEqual(artist.name, "Cypress Hill")
        self.assertTrue(artist.is_primary)


class TestManagementCommand(TestCase):

    def test_fails_with_no_arguments(self):
        self.assertRaises(CommandError, call_command, 'import_xml_file')

    def test_fails_with_nonexistent_file(self):
        self.assertRaises(CommandError, call_command, 'import_xml_file', 'bla')

    def test_fails_with_invalid_file(self):
        self.assertRaises(CommandError, call_command, 'import_xml_file',
                          'mobile_products/integration/invalid_example.xml')

    def test_successds_with_valid_file(self):
        call_command('import_xml_file',
                     'mobile_products/integration/example.xml')
