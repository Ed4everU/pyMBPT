import spglib
import numpy as np
from pyMBPT.structure.structure import crystal_structure

class symesh:

    def __init__(self, 
        crystal_info: crystal_structure, 
        k_density: tuple, 
        is_shift: list = [0,0,0]
    ):
        self.k_density = np.array(k_density)
        self.is_shift = is_shift 
        self.cell = crystal_info.cell
        self.space_group = spglib.get_spacegroup(self.cell, symprec=1e-5)

        self.mapping, self.int_k_points = \
            spglib.get_ir_reciprocal_mesh(k_density, self.cell, is_shift = self.is_shift)

        self.ire_int_k_points = self.int_k_points[np.unique(self.mapping),:]
        self.k_points = np.empty_like(self.int_k_points)
        self.ire_k_points = np.empty_like(self.ire_int_k_points)

        for ii in range(3):
            self.k_points[:,ii] = self.int_k_points[:,ii] / self.k_density[ii]
            self.ire_k_points[:,ii] = self.ire_int_k_points[:,ii] / self.k_density[ii]

        self.n_ire_k_points = self.ire_k_points.shape[0]
        self.n_k_points = self.k_points.shape[0]

    def show_symmetry_information():

        pass