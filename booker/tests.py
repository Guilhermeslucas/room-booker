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
        expected_response = [{'end': '2018-04-10T21:00:00Z', 'title': 'luizalabs meeting', 'begin': '2018-04-10T20:00:00Z', 'pk': 1, 'room': {'description': 'large', 'level': 1, 'id': 1, 'name': 'quaresma'}}]
        
        self.assertEqual(response_meeting_list.json(), expected_response)
    
    def test_change_meeting_info(self):
        pass

    def test_change_room_info(self):
        pass

    def test_delete_room(self):
        post_data = {'name': 'quaresma','level': 1,'description': 'large'}
        Room.objects.create(**post_data)

        response_room = client.delete('/booker/rooms/1/')

        self.assertEqual(200, response_room.status_code)

        response_after_deleted = client.get('/booker/rooms/')

        self.assertEqual(response_after_deleted.json(), [])

    def test_delete_room_not_exits(self):
        response_room = client.delete('/booker/rooms/1/')
        
        self.assertEqual(404, response_room.status_code)

    def test_delete_meeting(self):
        room_data = {'name': 'quaresma','level': 1,'description': 'large'}
        Room.objects.create(**room_data)

        post_data =  {'begin': '2018-04-10 20:00:00','end': '2018-04-10 21:00:00','title': 'luizalabs meeting','room_pk': 1}
        response_room = client.post('/booker/reservations/', json.dumps(post_data), content_type="application/json")

        response_after_deleted = client.delete('/booker/reservations/1/')

        self.assertEqual(response_after_deleted.status_code, 200)

        response_list_meetings = client.get('/booker/reservations/')

        self.assertEqual([], response_list_meetings.json())

    def test_delete_meeting_not_exists(self):
        response_after_deleted = client.delete('/booker/reservations/1/')

        self.assertEqual(404, response_after_deleted.status_code)

    def test_two_meetings_ok(self):
        room_data = {'name': 'quaresma','level': 1,'description': 'large'}
        Room.objects.create(**room_data)

        post_data =  {'begin': '2018-04-10 20:00:00','end': '2018-04-10 21:00:00','title': 'luizalabs meeting','room_pk': 1}
        response_first_reservation = client.post('/booker/reservations/', json.dumps(post_data), content_type="application/json")

        post_data =  {'begin': '2018-04-10 21:00:00','end': '2018-04-10 22:00:00','title': 'luizalabs meeting','room_pk': 1}
        response_second_reservation = client.post('/booker/reservations/', json.dumps(post_data), content_type="application/json")

        self.assertEqual(response_second_reservation.status_code, 201)
    
    def test_two_meetings_conflict(self):
        room_data = {'name': 'quaresma','level': 1,'description': 'large'}
        Room.objects.create(**room_data)

        post_data =  {'begin': '2018-04-10 20:00:00','end': '2018-04-10 21:00:00','title': 'luizalabs meeting','room_pk': 1}
        response_first_reservation = client.post('/booker/reservations/', json.dumps(post_data), content_type="application/json")

        post_data =  {'begin': '2018-04-10 20:00:00','end': '2018-04-10 20:30:00','title': 'luizalabs meeting','room_pk': 1}
        response_second_reservation = client.post('/booker/reservations/', json.dumps(post_data), content_type="application/json")

        self.assertEqual(response_second_reservation.status_code, 409)