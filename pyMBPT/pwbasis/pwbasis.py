import numpy as np
from mpi4py import MPI

class pw_basis:

    def __init__(self, 
        fft_size: tuple, 
        encut: float, 
        k_density : tuple,

        comm : MPI.Comm
        ):

        ## Global grid information
        self.fft_size = fft_size
        self.encut = encut
        self.kdense = k_density
        self.comm = comm

        ## MPI-local information
        # local kpoints
        self.kpoints 