import time

class Seats:
    @classmethod
    def init_seats(cls, rows, cols):
        seats = []
        for i in range(1, rows + 1):
            rows_seats = []
            for j in range(1, cols + 1):
                rows_seats.append('X')
            seats.append(rows_seats)
        return seats

class StarCinema:
    hall_lists = []

    @classmethod
    def entry_hall(cls, hall):
        cls.hall_lists.append(hall)

class Hall:
    def __init__(self, rows, cols, hall_no):
        self.show_list = []
        self.seats = {}
        self.cols = cols
        self.rows = rows
        self.hall_no = hall_no

        StarCinema.entry_hall(self)

    def book_seats(self, id, seat_list):
        show_id = [show[0] for show in self.show_list]
        if id not in show_id:
            print("Id Not Found.")
            return
        
        for row, col in seat_list:
            if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
                print('No seat Found')
                return

            if self.seats[id][row][col] == 'Y':
                print("Seat Already Soled.")
                return

            self.seats[id][row][col] = 'Y'
            print('Seat booking successful!')
    def entry_show(self, id, movieName, time):
        show_time = (id, movieName, time)
        self.show_list.append(show_time)
        self.seats[id] = Seats.init_seats(self.rows, self.cols)

    def view_show_list(self):
        for m in self.show_list:
            show_id, movieName, time = m
            print(f"Show ID: {show_id}, Movie: {movieName}, Time: {time}")

    def view_available_seats(self, id):
        show_id = [show[0] for show in self.show_list]

        if id not in show_id:
            print("Please provide a correct ID.")
            return

        ids = show_id.index(id)

        print(f"Available seats for Show ID {id}:")
        for row in range(self.rows):
            for col in range(self.cols):
                if self.seats[id][row][col] == 'X':
                    print(f"Seat ({row}, {col})")

    def view_booked_seats(self, id):
        print("***** Booked tickets ********:")
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.seats[id][row][col], end=" ")

xero = Hall(4, 4, 111)
xero.entry_show(1, "Poran", time.ctime())
xero.entry_show(2, "Paglu", time.ctime())
xero.entry_show(3, "Titanic", time.ctime())

while True:
    print()
    print('*****************.........*******************')
    print()
    print('1. Enter 1 for Show List')
    print('2. Enter 2 for Available Seats')
    print('3. Enter 3 for Seat Booking')
    print('4. Enter 4 for Close the Application')
    print()
    print('*****************.........*******************')
    option = int(input('Enter option:-> '))

    if option == 1:
        xero.view_show_list()
    elif option == 2:
        show_id = int(input('Enter show ID:-> '))
        xero.view_available_seats(show_id)
    elif option == 3:
        show_id = int(input('Enter show ID:-> '))
        seat_row = int(input('Enter seat row:-> '))
        seat_col = int(input('Enter seat column:-> '))
        xero.book_seats(show_id, [(seat_row, seat_col)])
    elif option == 4:
        break
    else:
        print('No match found.')
