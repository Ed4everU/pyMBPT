import psutil
import numba
import logging
from datetime import datetime
from pyMBPT.mpi import Comm
from pyMBPT.format import Format



class Log:

    def __init__(self,
        comm: Comm,
        level: str = 'DEBUG',
        filename: str = 'pyMBPT.log',
    ) -> None:
        self.comm = comm
        self.log = logging.getLogger()
        self.log.setLevel(level)
        console_stream = logging.StreamHandler()
        file_stream = logging.FileHandler(filename,'w')
        self.log.addHandler(console_stream)
        self.log.addHandler(file_stream)
    
    def log_time(self):
        now = datetime.now()
        if self.comm.is_root:
            self.log.info('Date: {}.{}.{}  ~ {}'.format(
                now.strftime("%Y"), now.strftime("%m"), now.strftime("%d"),
                now.strftime("%H:%M:%S"))
            )

    def log_system_infor(self, is_gpu: bool):
        ncore = self.comm.size
        nthread = numba.get_num_threads()#config.NUMBA_NUM_THREADS
        
        if self.comm.is_root:
            self.log_time()
            self.log.info('Running On {} Cores ({} Threads Each Core)'.format(ncore, nthread))


    def log_memory_infor(self):
        if self.comm.is_root:
            self.log.info(
                """
                
                """
            )

