from unittest import TestCase

import audioanalytics


class TestJoke(TestCase):
    def test_is_string(self):
        s = audioanalytics.extract_feature()
        self.assertTrue(isinstance(s, basestring))
