import pickle
import os
import zipfile

def data_hotel(hotel_list):
    with open('hotel.pkl', 'wb') as f:
        pickle.dump(hotel_list, f, pickle.HIGHEST_PROTOCOL)
        
def data_rooms(rooms_list):
    with open('guests.pkl', 'wb') as f:
        pickle.dump(rooms_list, f, pickle.HIGHEST_PROTOCOL)

def data_staffs(staff_list):
    with open('staff.pkl', 'wb') as f:
        pickle.dump(staff_list, f, pickle.HIGHEST_PROTOCOL)

def data_guests(guest_list):
    with open('guests.pkl', 'wb') as f:
        pickle.dump(guest_list, f, pickle.HIGHEST_PROTOCOL)

def data_reservations(reservation_list):
    with open('reservations.pkl', 'wb') as f:
        pickle.dump(reservation_list, f, pickle.HIGHEST_PROTOCOL)

def zip_data():
    with zipfile.ZipFile('data.dat','w',compression=zipfile.ZIP_DEFLATED) as zip:
        zip.write('hotel.pkl')
        zip.write('staff.pkl')
        zip.write('guests.pkl')
        zip.write('rooms.pkl')
        zip.write('reservations.pkl')
        zip.close()
    os.remove('hotel.pkl')
    os.remove('staff.pkl')
    os.remove('guests.pkl')
    os.remove('rooms.pkl')
    os.remove('reservations.pkl')


def open_hotel():
    hotel_list = []
    if (os.path.exists('hotel.pkl')):
        with open('hotel.pkl', 'rb') as f:
            hotel_list = pickle.load(f)
    return hotel_list

def open_room():
    room_list = []
    if (os.path.exists('room.pkl')):
        with open('room.pkl', 'rb') as f:
            room_list = pickle.load(f)
    return room_list

def open_staffs():
    staff_list = []
    if (os.path.exists('staff.pkl')):
        with open('staff.pkl', 'rb') as f:
            staff_list = pickle.load(f)
    return staff_list

def open_guests():
    guest_list = []
    if (os.path.exists('guests.pkl')):
        with open('guests.pkl', 'rb') as f:
            guest_list = pickle.load(f)
    return guest_list

def open_reservations():
    reservation_list = []
    if (os.path.exists('reservations.pkl')):
        with open('reservations.pkl', 'rb') as f:
            reservation_list = pickle.load(f)
    return reservation_list

def unzip_data():
    if (os.path.exists('data.dat')):
        with zipfile.ZipFile('data.dat','r') as zip:
            zip.extractall()
        os.remove('data.dat')