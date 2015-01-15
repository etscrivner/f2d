# -*- coding: utf-8 -*-
import unittest

from tracks import entities


class IsValidTest(unittest.TestCase):

    def test_should_consider_soundcloud_valid(self):
        """Should consider SoundCloud valid"""
        self.assertTrue(
            entities.TrackType.is_valid(entities.TrackType.SoundCloud)
        )

    def test_should_consider_dropbox_valid(self):
        """Should consider DropBox valid"""
        self.assertTrue(
            entities.TrackType.is_valid(entities.TrackType.DropBox)
        )

    def test_should_not_consider_invalid_value_valid(self):
        """Should not consider invalid value valid"""
        self.assertFalse(
            entities.TrackType.is_valid(123)
        )
