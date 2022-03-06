from django.test import TestCase

from .urlutils import add_url_protocol


class UrlUtilsTestCase(TestCase):
    def test_add_url_protocol_missing_protocol(self):
        # Arrange
        url_missing_protocol = "www.example.com"
        expected_result = "https://www.example.com"

        # Act
        actual_result = add_url_protocol(url_missing_protocol)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_add_url_protocol_http_protocol(self):
        # Arrange
        http_url = "http://example.com"
        expected_result = http_url

        # Act
        actual_result = add_url_protocol(http_url)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_add_url_protocol_https_protocol(self):
        # Arrange
        https_url = "https://example.com"
        expected_result = https_url

        # Act
        actual_result = add_url_protocol(https_url)

        # Assert
        self.assertEqual(expected_result, actual_result)
