import numpy as np

class atom():

    def __init__(self, element_name: str = "", mass: float = 0.5, crystal_coordinate:np.array = np.zeros(3)):

        self.element = element_name
        self.mass = mass
        self.crystal_coordinate = crystal_coordinate

    def crystal_to_direct(a : np.array):

        pass