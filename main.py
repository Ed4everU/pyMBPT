from pyMBPT.log import Log
from pyMBPT.mpi import Comm


comm = Comm()

log = Log(comm)
log.log_system_infor()
