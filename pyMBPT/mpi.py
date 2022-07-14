from mpi4py import MPI



class Comm:

    def __init__(self) -> None:
        self.comm = MPI.COMM_WORLD

    @property
    def have_group(self):
        pass

    @property
    def rank(self):
        return self.comm.Get_rank()

    @property
    def size(self):
        return self.comm.Get_size()

    @property
    def is_root(self):
        return self.rank == 0

    @classmethod
    def Send(self, buf, dest, tag=0):
        """ blocking send """
        self.comm.Send(buf, dest, tag)

    @classmethod
    def Bcast(self, buf, root=0):
        """ broadcast a message from one process to all other processes in a group """
        self.comm.Bcast(buf, root)