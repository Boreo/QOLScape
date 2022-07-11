####################
# Copyright (c) 2022, Boreo <hhttps://github.com/Boreo>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.                         
#                                                                                   
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND   
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED     
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE            
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR   
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES    
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;      
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND       
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT        
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS     
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.                      
####################


from time import time
from modules.pixelcolour import getPixel
from config import MainConfig as mcfg
import pyautogui

class Metronomer():
    """Object to find and store location and colour of the metronome overlay
    
    Args:
        windowName (str)(optional): Name of Runelite window name. Defaults to "RuneLite".
    
    Attributes:
        x (int): the x position of metronome
        y (int): the y position of metronome
        colour (tuple): two colours of metronome as a hex string ARGB
        
    Methods:
        getXY(): Returns x and y position of the metronome as tuple
        getColour(): Returns the two colours of the metronome as tuple.
        selectMetronome(): Select the metronome location
        getMetronome(): Find the metronome location using image recognition
    
    """
      
    def __init__(self, windowName = "RuneLite"):
        self.windowName = windowName
        self.x = None
        self.y = None
        self.colour = None
        
    def getXY(self):
        return (self.x, self.y)
    
    def getColour(self):
        return self.colour
    
    def getMetronome(self):
        if mcfg.useWindow:
            flick1 = pyautogui.locateOnWindow(".\\resources\\flick1.png", self.windowName, grayscale = True, confidence = .8)
            flick2 = pyautogui.locateOnWindow(".\\resources\\flick2.png", self.windowName, grayscale = True, confidence = .8)
        else:
            flick1 = pyautogui.locateOnScreen(".\\resources\\flick1.png", grayscale = True, confidence = .8)
            flick2 = pyautogui.locateOnScreen(".\\resources\\flick2.png", grayscale = True, confidence = .8)
            
        if flick1 != None:
            self.x = flick1[0]
            self.y = flick1[1]
            self._findMetroColour(self.x, self.y)
        elif flick2 != None:
            self.x = flick2[0]
            self.y = flick2[1]
            self._findMetroColour(self.x, self.y)
        else:
            raise self.CouldNotFind("Could not find metronome location")

    def _findMetroColour(self, x, y):
        timeout = time() + 5
        colour1 = getPixel(x,y)
        while True:
            if colour1 != getPixel(x,y):
                colour2 = getPixel(x,y)
                self.colour = (colour1, colour2)
                break
            if time() > timeout:
                raise self.CouldNotFind("Could not find metronome colours")

    class CouldNotFind(Exception):
        pass
        

if __name__ == "__main__":
    pass