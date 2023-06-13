import requests
import json


class Booking:
    url = 'https://restful-booker.herokuapp.com'

    def create_token(self, token):
        #Create Token

        headers = {
            'Content-Type': 'application/json'
        }
        data = json.dumps(token)
        return requests.post(self.url + '/auth', headers=headers, data=data)


    def get_booking_ids(self, token, filter):
        #Get Booking ID

        headers = {
            'Accept': 'application/json'
        }
        return requests.get(self.url + f'/booking', headers=headers, params=filter)


    def get_booking(self, token, booking_id):
        #Get Booking

        headers = {
            'Accept': 'application/json'
        }
        return requests.get(self.url + f'/booking/{booking_id}', headers=headers)


    def create_booking(self, token, booking):
        #Create Booking

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        data = json.dumps(booking)
        return requests.post(self.url + '/booking', headers=headers, data=data)


    def update_booking(self, token, booking_id, booking):
        #Update Booking

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Cookie': f'{token}',
            'Authorization': 'YWRtaW46cGFzc3dvcmQxMjM=',
        }
        data = json.dumps(booking)
        return requests.put(self.url + f'/booking/{booking_id}', headers=headers, data=data)


    def partial_update_booking(self, token, booking_id, booking):
        #Partial Update Booking

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Cookie': f'{token}',
            'Authorization': 'YWRtaW46cGFzc3dvcmQxMjM=',
        }
        data = json.dumps(booking)
        return requests.patch(self.url + f'/booking/{booking_id}', headers=headers, data=data)


    def delete_booking(self, token, booking_id):
        #Delete Booking
        headers = {
            'Cookie': f'{token}',
            'Authorization': 'YWRtaW46cGFzc3dvcmQxMjM=',
        }
        return requests.delete(self.url + f'/booking/{booking_id}', headers=headers)


my_booking = Booking()
