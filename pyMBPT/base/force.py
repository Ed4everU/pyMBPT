class ForceConstant:

    _3rd_fc_str_ = """
    X _ _
        {:10.6f}    {:10.6f}    {:10.6f}
        {:10.6f}    {:10.6f}    {:10.6f}
        {:10.6f}    {:10.6f}    {:10.6f}
    Y _ _
        {:10.6f}    {:10.6f}    {:10.6f}
        {:10.6f}    {:10.6f}    {:10.6f}
        {:10.6f}    {:10.6f}    {:10.6f}
    Z _ _
        {:10.6f}    {:10.6f}    {:10.6f}
        {:10.6f}    {:10.6f}    {:10.6f}
        {:10.6f}    {:10.6f}    {:10.6f}
    """

    _4th_fc_str_ = """

    X X _ _
        {:10.6f}    {:10.6f}    {:10.6f}
        {:10.6f}    {:10.6f}    {:10.6f}
        {:10.6f}    {:10.6f}    {:10.6f}
    X Y _ _
        {:10.6f}    {:10.6f}    {:10.6f}
        {:10.6f}    {:10.6f}    {:10.6f}
        {:10.6f}    {:10.6f}    {:10.6f}
    X Z _ _
        {:10.6f}    {:10.6f}    {:10.6f}
        {:10.6f}    {:10.6f}    {:10.6f}
        {:10.6f}    {:10.6f}    {:10.6f}

    Y X _ _
        {:10.6f}    {:10.6f}    {:10.6f}
        {:10.6f}    {:10.6f}    {:10.6f}
        {:10.6f}    {:10.6f}    {:10.6f}
    Y Y _ _
        {:10.6f}    {:10.6f}    {:10.6f}
        {:10.6f}    {:10.6f}    {:10.6f}
        {:10.6f}    {:10.6f}    {:10.6f}
    Y Z _ _
        {:10.6f}    {:10.6f}    {:10.6f}
        {:10.6f}    {:10.6f}    {:10.6f}
        {:10.6f}    {:10.6f}    {:10.6f}

    Z X _ _
        {:10.6f}    {:10.6f}    {:10.6f}
        {:10.6f}    {:10.6f}    {:10.6f}
        {:10.6f}    {:10.6f}    {:10.6f}
    Z Y _ _
        {:10.6f}    {:10.6f}    {:10.6f}
        {:10.6f}    {:10.6f}    {:10.6f}
        {:10.6f}    {:10.6f}    {:10.6f}
    Z Z _ _
        {:10.6f}    {:10.6f}    {:10.6f}
        {:10.6f}    {:10.6f}    {:10.6f}
        {:10.6f}    {:10.6f}    {:10.6f}

    """

    def __init__(self) -> None:
        pass
    
    
    @classmethod
    def print_3rd_FC(self, PHI, log):
        log.info(
            self._3rd_fc_str_.format(
                PHI[0,0], PHI[0,1], PHI[0,2],
                PHI[1,0], PHI[1,1], PHI[1,2],
                PHI[2,0], PHI[2,1], PHI[2,2]
            )
        )

    @classmethod
    def print_4th_FC(self, PHI, log):
        log.info(
            self._4th_fc_str_.format(
                
            )
        )