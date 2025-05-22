from django.test import TestCase

# Create your tests here.
# your_app/tests.py
from django.test import TestCase
from learn.factories import HotspotFactory, EventFactory

class HotspotModelTest(TestCase):
    def test_hotspot_creation(self):
        hotspot = HotspotFactory()  # Creates and saves a dummy Hotspot
        self.assertEqual(hotspot.__class__.__name__, "Hotspot")

class EventModelTest(TestCase):
    def test_event_has_hotspot(self):
        event = EventFactory()  # Creates Event + linked Hotspot automatically
        self.assertTrue(event.hotspot.pk)  # Check if hotspot exists