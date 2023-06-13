
def prepare_data(arg):
    """
    Метод подготовки тестовых данных
    """

    global data
    if arg == 'booking':
        data = {
            'firstname': 'Jo',
            'lastname': 'Travolta',
            'totalprice': 100,
            'depositpaid': True,
            'bookingdates': {
                'checkin': '2023-05-01',
                'checkout': '2023-05-15'
            },
            'additionalneeds': 'Breakfast'
        }
    elif arg == 'full_change_booking':
        data = {
            'firstname': 'John',
            'lastname': 'Travolta',
            'totalprice': 200,
            'depositpaid': True,
            'bookingdates': {
                'checkin': '2023-05-01',
                'checkout': '2023-05-31'
            },
            'additionalneeds': 'Mini BAR'
        }
    elif arg == 'part_change_booking':
        data = {
            'totalprice': 150,
            'bookingdates': {
                'checkout': '2023-05-25'
            },
        }
    elif arg == 'token':
        data = {
            'username': 'admin',
            'password': 'password123'
        }
    elif arg == 'filter':
        data = {
            'firstname': 'John'
        }
    return data
