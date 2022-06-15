"""Write functions for common real estate equations."""

___author___ = "Diego Cardenas"

class SingleFamily:
    """Create class that represents single family home with key metrics."""
    NAME: str
    GLA: float
    NOI: float
    MKT_VAL: float

    def __init__(self, name: str, glai: int, noii: int, mkt_vali: float):
        self.NAME = name
        self.GLA = glai
        self.NOI = noii
        self.MKT_VAL = mkt_vali
    
    def __repr__(self) -> list[str]:
        return_list = []
        return_list.append(self.NAME)
        return_list.append(self.GLA)
        return_list.append(self.NOI)
        return_list.append(self.MKT_VAL)
    
    def cap_rate(self, top: float, bot: float) -> str:
        top = self.NOI
        bot = self.MKT_VAL
        num: float = top/bot
        return (str(num) + "%")

    




