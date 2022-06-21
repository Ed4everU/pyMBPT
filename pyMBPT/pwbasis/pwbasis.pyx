
import numpy as np
#from mpi4py cimport MPI

cdef class PWbasis:

    def __init__(self, tuple fft_size, float encut, tuple kdense):
        

        ## Global grid information
        self.fft_size = fft_size
        self.encut = encut
        self.kdense = kdense

        ## MPI-local information
        ## kpoints

    def getMesh(self):

        pass
    