from abc import ABC

class Agent(ABC):

    @abstractmethod
    def get_action(self):
        pass