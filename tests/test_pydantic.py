from api.client import my_booking
from resources.prepare_data import prepare_data
from serializers.orders import *

token = ''
booking_id = 0


def test_create_token():
    #Create Token

    global token

    new_token = my_booking.create_token(prepare_data('token'))
    token = new_token.json()['token']
    assert new_token.status_code == 200, f'{new_token.json()}'
    assert Token(**new_token.json()).dict()
    assert token != ''


def test_get_booking_ids():
    #Get Booking ID

    filter = prepare_data('filter')
    assert FilterModel(**filter).dict()

    test_get_booking_ids = my_booking.get_booking_ids(token, filter)
    assert test_get_booking_ids.status_code == 200, f'{test_get_booking_ids.json()}'


def test_get_booking():
    #Get Booking

    global booking_id

    if booking_id != 0:
        pass
    else:
        filter = []
        list_of_bookings = my_booking.get_booking_ids(token, filter)
        booking_id = list_of_bookings.json()[0]['bookingid']
    get_booking = my_booking.get_booking(token, booking_id)

    assert get_booking.status_code == 200, f'{get_booking.json()}'
    assert BookingModel(**get_booking.json()).dict()


def test_create_booking():
    #Create Booking

    global booking_id

    booking = prepare_data('booking')
    create_booking = my_booking.create_booking(token, booking)
    booking_id = create_booking.json()['bookingid']

    get_booking = my_booking.get_booking(token, booking_id)

    assert get_booking.status_code == 200, f'{get_booking.json()}'
    assert BookingModel(**booking).dict() == BookingModel(**get_booking.json()).dict()


def test_update_booking():
    #Update Booking

    global booking_id

    if booking_id != 0:
        pass
    else:
        filter = []
        list_of_bookings = my_booking.get_booking_ids(token, filter)
        booking_id = list_of_bookings.json()[0]['bookingid']

    booking = prepare_data('full_change_booking')
    update_booking = my_booking.update_booking(token, booking_id, booking)

    assert update_booking.status_code == 200, f'{update_booking.json()}'
    assert BookingModel(**booking).dict() == BookingModel(**update_booking.json()).dict()


def test_partial_update_booking():
    #Partial Update Booking

    global booking_id

    if booking_id != 0:
        pass
    else:
        filter = []
        list_of_bookings = my_booking.get_booking_ids(token, filter)
        booking_id = list_of_bookings.json()[0]['bookingid']

    booking = prepare_data('part_change_booking')
    partial_update_booking = my_booking.partial_update_booking(token, booking_id, booking)

    assert partial_update_booking.status_code == 200, f'{partial_update_booking.json()}'
    assert LiteBookingModel(**booking).dict() == LiteBookingModel(**partial_update_booking.json()).dict()


def test_delete_booking():
    #Delete Booking

    global booking_id

    if booking_id != 0:
        pass
    else:
        filter = []
        list_of_bookings = my_booking.get_booking_ids(token, filter)
        booking_id = list_of_bookings.json()[0]['bookingid']

    delete_booking = my_booking.delete_booking(token, booking_id)

    assert delete_booking.status_code == 200, f'{delete_booking.url}'
