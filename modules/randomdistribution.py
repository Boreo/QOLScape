import random, math


def randomDelay(minD,maxD,dev,tar,weighted = True):
    """Returns a distributed random number to be more human-like

    Args:
        minD (int): Lower Floor(min) of return
        maxD (int): Upper floor(max) of return
        dev (int): Spread of return, away from mean
        tar (int): Target for mean
        weighted (bool, optional): Whether distribution should be weighted to the left (spreads more to the right). 
            Defaults to True.

    Returns:
        float: Random value
    """
    if weighted:
        return clamp(minD,maxD,-math.log(abs(random.gauss(0,1))) * dev + tar)
    if not weighted:
        return clamp(round(random.gauss(0,1) * dev + tar))
    
def clamp(minD,maxD,val):
    return max(minD,min(maxD,val))/1000