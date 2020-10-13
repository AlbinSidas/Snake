class Agent_Interface():

    # Dependencyinjection
    def __init__(self, model): 
        self.model = model

    def get_action(self, world_list, python, fruit, pygame):
        return self.model.get_action(world_list, python, fruit, pygame)
        