from django.test import TestCase, Client
import json
# Create your tests here.
client = Client()

class bookerTest(TestCase):
    def test_create_room_and_get_back_ok(self):
        post_data = {'name': 'quaresma','level': 1,'description': 'large'}
        response = client.post('/booker/rooms/', post_data)
        self.assertEqual({'name': 'quaresma','level': 1,'description': 'large', 'pk': 1 }, response.json())
    
    def test_create_meeting_valid_room(self):
        pass
    
    def test_create_meeting_invalid_room(self):
        pass

    def test_list_rooms(self):
        pass
    
    def test_list_meetings(self):
        pass
    
    def test_change_meeting_info(self):
        pass

    def test_change_room_info(self):
        pass

    def test_delete_room(self):
        pass
    
    def test_delete_meeting(self):
        pass

    def test_create_valid_meeting(self):
        pass

    def test_create_invalid_meeting(self):
        pass