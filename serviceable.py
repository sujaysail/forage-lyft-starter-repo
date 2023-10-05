from abc import ABC, abstractmethod

class Serviceable(ABC):
    @abstractmethod
    def neeeds_service(self):
        pass