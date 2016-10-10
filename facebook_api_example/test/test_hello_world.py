from unittest import TestCase

from facebook_api_example.app.hello_world import HELLO_WORLD_MESSAGE
from facebook_api_example.app.hello_world import get_message


class TestHelloWorld(TestCase):
    def test_get_message(self):
        assert HELLO_WORLD_MESSAGE == get_message()
