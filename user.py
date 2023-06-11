from abc import ABC, abstractmethod
from unicodedata import name


class User(ABC):
    def __init__(self, name, email, nid) -> None:
        self.name = name
        self.email = email
        # Todo: set user id dynamicly
        self.__id = 0
        self.__nid = nid
        self.wallet = 0

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError


class Rider(User):
    def __init__(self, name, email, nid) -> None:
        self.current_ride = None
        super().__init__(name, email, nid)

    def display_profile(self):
        print(f'Rider : with name: {self.name} with email:{self.email}')

    def request_ride(self, location, destination):
        if not self.current_ride:
            # To do:Set ride properly
            # TODO: set current ride via ride match
            ride_request = None


class Driver(User):
    def __init__(self, name, email, nid, current_location) -> None:
        super().__init__(name, email, nid)
        self.current_location = current_location

    def display_profile(self):
        print(f'Rider : with name: {self.name} with email:{self.email}')

    def accept_ride(self, ride):
        ride.set_Driver(self)
