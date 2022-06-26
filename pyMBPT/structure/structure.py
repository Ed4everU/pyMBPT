import spglib
import numpy as np
from pyMBPT.structure.atom import atom


class crystal_structure():

    def __init__(self, 
        a: np.array = np.zeros(3), 
        b: np.array = np.zeros(3),
        atom_mass: np.array = np.zeros(3), 
        atom_element: np.array = np.zeros(3),
        atom_num_each_elem: np.array = np.zeros(3),
        crystal_coordinates: list[np.array] = [np.zeros(3),np.zeros(3),np.zeros(3)],
        atom_list: list[atom] = []
    ):
        self.a = a
        self.b = b
        self.atom_mass = atom_mass
        self.atom_element = atom_element
        self.atom_num_each_elem = atom_num_each_elem
        self.crystal_coordinates = crystal_coordinates
        self.atom_list = atom_list

        temp_num_ls = []
        for ii in range(len(self.atom_element)):
            for jj in range(self.atom_num_each_elem[ii]):
                temp_num_ls.append(ii+1)

        ## cell for spglib
        self.cell = (self.a, self.crystal_coordinates, temp_num_ls)


    def from_poscar(self, file : str, elem_mass : tuple):

        with open(file) as f:

            lines = f.read().splitlines()
            scale = float(lines[1])

            a = np.zeros((3,3)) 
            a[0,:] = np.array(list(map(float,lines[2].strip().split())))*scale
            a[1,:] = np.array(list(map(float,lines[3].strip().split())))*scale
            a[2,:] = np.array(list(map(float,lines[4].strip().split())))*scale

            b = np.zeros((3,3))
            b[0,:] = 2 * np.pi * (np.cross(a[1,:],a[2,:]))/(np.dot(a[0,:],np.cross(a[1,:],a[2,:])))
            b[1,:] = 2 * np.pi * (np.cross(a[2,:],a[0,:]))/(np.dot(a[1,:],np.cross(a[2,:],a[0,:])))
            b[2,:] = 2 * np.pi * (np.cross(a[0,:],a[1,:]))/(np.dot(a[2,:],np.cross(a[0,:],a[1,:])))

            atom_elem = np.array(lines[5].strip().split())
            atom_num_each_elem = np.array(list(map(int,lines[6].strip().split())))
            natom = np.sum(atom_num_each_elem)

            atom_mass = np.zeros(natom)
            crystal_coordinates = []
            atom_list = []

            for ii in range(atom_elem.shape[0]):
                for jj in range(atom_num_each_elem[ii]):

                    this_crystal_coordinate = np.array(list(map(float, lines[8+np.sum(atom_num_each_elem[:ii])+jj].strip().split())))
                    atom_mass[np.sum(atom_num_each_elem[:ii])+jj] = elem_mass[ii]
                    crystal_coordinates.append(this_crystal_coordinate)
                    atom_list.append(atom(atom_elem[ii], atom_mass[ii], this_crystal_coordinate))

            return crystal_structure(a, b, atom_mass, atom_num_each_elem, crystal_coordinates, atom_list)
            

    def get_symmetry(self, verbose: bool):

        if verbose:

            print()

        pass