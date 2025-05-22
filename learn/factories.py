# your_app/factories.py
import factory
from django.contrib.auth import get_user_model
from learn.models import Hotspot, Event  # Replace with your actual models

User = get_user_model()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Faker("user_name")
    email = factory.Faker("email")
    is_active = True

class HotspotFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Hotspot
    name = factory.Faker("city")  # Random city name
    location = factory.Faker("address")
    is_active = factory.Faker("boolean")
    created_by = factory.SubFactory(UserFactory)  # Links to a fake user

class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event
    title = factory.Faker("sentence")
    date = factory.Faker("future_date")
    hotspot = factory.SubFactory(HotspotFactory)  # Links to a fake hotspot