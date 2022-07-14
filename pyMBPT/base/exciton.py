import numpy as np
from pyMBPT.base.quasiparticle import QuasiParticle
from typing import Union, Tuple, List


class Exciton(QuasiParticle):

    
    """
    :Asvck - the exciton's envelope function [nsb, nvb, ncb, nvk]
    :vk    - the hole's mesh
    :seng  - the exciton's energy
    :vb    - the valence band indices
    :cb    - the conduction band indices
    :sb    - the exciton band indices
    """
    

    def __init__(self,
        Asvck: Union[None,np.ndarray] = None,
        vk: Union[None,np.ndarray] = None,
        seng: Union[None,np.ndarray] = None,
        vb: Union[None,Tuple,List,np.ndarray] = None,
        cb: Union[None,Tuple,List,np.ndarray] = None,
        sb: Union[None,Tuple,List,np.ndarray] = None,
    ) -> None:
        super.__init__(_type_ = 'exciton')
        

    

    