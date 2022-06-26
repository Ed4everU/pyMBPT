import numpy as np
from mpi4py import MPI
from pyMBPT.pwbasis.symesh import symesh

class pw_basis:

    def __init__(self, 
        fft_size: tuple, 
        encut: float, 
        k_density : tuple,
        is_reduce : bool,
        mesh : symesh,
        comm : MPI.Comm
        ):

        ## Global grid information
        self.fft_size = fft_size
        self.encut = encut
        self.kdense = k_density
        self.is_reduce = is_reduce
        self.mesh = mesh
        self.comm = comm
        self.rank = comm.Get_rank()
        self.ncpu = comm.Get_size()
        

        ## MPI-local information
        # local kpoints
        if is_reduce:
            self.local_k_id = [ ik for ik in range(self.mesh.n_ire_k_points) if ik%self.ncpu == self.rank]
            self.k_points_local = self.mesh.ire_k_points[self.local_k_id,:]
            self.int_k_points_local = self.mesh.ire_int_k_points[self.local_k_id,:]
        else:
            self.local_k_id = [ ik for ik in range(self.mesh.n_k_points) if ik%self.ncpu == self.rank]
            self.k_points_local = self.mesh.k_points[self.local_k_id,:]
            self.int_k_points_local = self.mesh.int_k_points[self.local_k_id,:]
        
    def show_k_points(self,):
        
        if self.rank == 0:
            if self.is_reduce:
                print("------------------ irreducible k-points -------------------")
                for ik in range(self.mesh.ire_k_points.shape[0]):
                    print("%6.4f %6.4f %6.4f".format(self.mesh.ire_k_points[ik,0], self.mesh.ire_k_points[ik,1], self.mesh.ire_k_points[ik,2]))
            else:
                print("------------------------ k-points -------------------------")
                for ik in range(self.mesh.k_points.shape[0]):
                    print("%6.4f %6.4f %6.4f".format(self.k_points[ik,0], self.k_points[ik,1], self.k_points[ik,2]))