class car:
    def __init__(self, reg_number, color):
        self.reg_number = reg_number
        self.color = color


class parkinglot:
    '''
    class ticket:
        def __init__(self, occupied, car_being_parked):
            # self.slotnumber = slotnumber
            self.occupied = occupied
            self.car_being_parked = car_being_parked
    '''

    def __init__(self, number_of_slots):
        self.number_of_slots = number_of_slots
        self.dict_of_parked_cars = {}
        self.num_of_cars_in_parking = 0
        print("Created a parking lot with ",number_of_slots," slots")
        # for i in range(number_of_slots):
        #     self.list_of_parked_cars.append(None)

    def park(self, reg_number, color):
        car_being_parked = car(reg_number, color)
        if int(self.num_of_cars_in_parking)<int(self.number_of_slots):
            nearest_freeslot = self.find_nearest_freeslot()
            # self.list_of_parked_cars[self.num_of_cars_in_parking] = self.issueticket(car_being_parked, nearest_freeslot)
            self.dict_of_parked_cars[nearest_freeslot] = car_being_parked
            print("Allocated slot number: ",nearest_freeslot)
            self.num_of_cars_in_parking+=1
        else:
            print("Sorry, parking lot is full")

    '''
    slots_occupied = {}
  
    def issueticket(self, car_being_parked, nearest_freeslot):
      # tkt = ticket(nearest_free_slot, True, car_being_parked)
      slots_occupied[nearest_free_slot] = car_being_parked
  
  
    def find_nearest_freeslot(self):
      i=1
      while True:
        try:
          slots_occupied[i]
          i+=1
        except:
          return i # returns the nearest free slot
    

    def issueticket(self, car_being_parked, nearest_freeslot):
        return self.ticket(nearest_freeslot, True, car_being_parked)
    '''

    def find_nearest_freeslot(self):
        i = 1
        while True:
            try:
                self.dict_of_parked_cars[i]
                i += 1
            except: # narrow down this exception
                return i
            '''
            if self.list_of_parked_cars[i] == None:
                return i
            '''

    def leave(self, slotnumber):
        try:
            del self.dict_of_parked_cars[slotnumber]
            print("Slot number ",slotnumber," is free")
            self.num_of_cars_in_parking -= 1
        except:
            print("Not Found")

    def status(self):
        print("Slot  "+"Registration  "+"Color")
        for x in self.dict_of_parked_cars:
            car = self.dict_of_parked_cars[x]
            print(x,"     ", car.reg_number, "      ", car.color) # have to change this

    def registration_numbers_for_cars_with_colour(self, color):
        found = False
        for x in self.dict_of_parked_cars:
            car = self.dict_of_parked_cars[x]
            if car.color == color :
                print(car.reg_number)
                found = True
        if (found == False):
            print("Not Found")

    def slot_numbers_for_cars_with_colour(self, color):
        found = False
        for x in self.dict_of_parked_cars:
            car = self.dict_of_parked_cars[x]
            if car.color == color :
                print(x)
                found = True
        if(found == False):
            print("Not Found")

    def slot_number_for_registration_number(self, reg_number):
        found = False
        for x in self.dict_of_parked_cars:
            car = self.dict_of_parked_cars[x]
            if car.reg_number == reg_number :
                print(car.reg_number)
                found = True
        if(found == False):
            print("Not Found")

default_parking_lot = None

def create_parking_lot(number_of_slots):
    global default_parking_lot
    default_parking_lot = parkinglot(number_of_slots)

while True:
    inp = input()
    split_input = inp.split()
    if inp.startswith("create_parking_lot "):
        create_parking_lot(split_input[1]) # regular expression to extract number from the command given
    elif inp.startswith("park "):
        default_parking_lot.park(split_input[1], split_input[2])
    elif inp.startswith("leave "):
        default_parking_lot.leave(int(split_input[1]))
    elif inp.startswith("status"):
        default_parking_lot.status()
    elif inp.startswith("registration_numbers_for_cars_with_colour "):
        default_parking_lot.registration_numbers_for_cars_with_colour(split_input[1])
    elif inp.startswith("slot_numbers_for_cars_with_colour "):
        default_parking_lot.slot_numbers_for_cars_with_colour(split_input[1])
    elif inp.startswith("slot_number_for_registration_number "):
        default_parking_lot.slot_number_for_registration_number(split_input[1])











