from django.test import TestCase, Client
import json
from .models import Room, Reservation

client = Client()

class bookerTest(TestCase):
    def test_create_room_and_get_back_ok(self):
        post_data = {'name': 'quaresma','level': 1,'description': 'large'}
        response = client.post('/booker/rooms/', post_data)
        post_data['pk'] = 1
        self.assertEqual(post_data, response.json())

    def test_create_meeting_valid_room(self):
        post_data = {'name': 'quaresma','level': 1,'description': 'large'}
        Room.objects.create(**post_data)

        post_data =  {'begin': '2018-04-10 20:00:00','end': '2018-04-10 21:00:00','title': 'luizalabs meeting','room_pk': 1}
        response = client.post('/booker/reservations/', json.dumps(post_data), content_type="application/json")

        self.assertEqual(201, response.status_code)
    
    def test_create_meeting_invalid_room(self):
        post_data =  {'begin': '2018-04-10 20:00:00','end': '2018-04-10 21:00:00','title': 'luizalabs meeting','room_pk': 1}
        response = client.post('/booker/reservations/', json.dumps(post_data), content_type="application/json")

        self.assertEqual(404, response.status_code)

    def test_list_rooms(self):
        room_data = {'name': 'quaresma','level': 1,'description': 'large'}
        Room.objects.create(**room_data)

        room_data['pk'] = 1

        response = client.get('/booker/rooms/')
        self.assertEqual(response.json(), [room_data])

    def test_list_meetings(self):
        room_data = {'name': 'quaresma','level': 1,'description': 'large'}
        Room.objects.create(**room_data)

        post_data =  {'begin': '2018-04-10 20:00:00','end': '2018-04-10 21:00:00','title': 'luizalabs meeting','room_pk': 1}
        response_room = client.post('/booker/reservations/', json.dumps(post_data), content_type="application/json")
        
        self.assertEqual(201, response_room.status_code)

        response_meeting_list = client.get('/booker/reservations/')

        print(response_meeting_list.json())
    
    def test_change_meeting_info(self):
        pass

    def test_change_room_info(self):
        pass

    def test_delete_room(self):
        pass
    
    def test_delete_meeting(self):
        pass

    def test_two_meetings_ok(self):
        pass
    
    def test_two_meetings_conflict(self):
        pass