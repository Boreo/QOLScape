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

from time import sleep
from pynput.keyboard import GlobalHotKeys
from sys import exit
from modules.metronome import Metronomer
from modules.randomdistribution import randomDelay, clamp
from modules.pixelcolour import getPixel
from config import AutoPrayFlickConfig as cfg
from config import MainConfig as mcfg
import random, math, threading, copy, pyautogui

#Pretty output

no = ("\033[91m" + "X" + "\033[0m")
ok = ("\033[92m" + "X" + "\033[0m")
wait = ("\033[93m" + "x" + "\033[0m")


def getOrbLoc():
    tries = 0
    while True:
        if mcfg.useWindow:
            prayOrbI = pyautogui.locateOnWindow(".\\resources\\prayerBInactive.png", mcfg.windowName, confidence = .8)
            prayOrbA = pyautogui.locateOnWindow(".\\resources\\prayerBActive.png", mcfg.windowName, confidence = .8)
        else:
            prayOrbI = pyautogui.locateOnScreen(".\\resources\\prayerBInactive.png", confidence = .8)
            prayOrbA = pyautogui.locateOnScreen(".\\resources\\prayerBActive.png", confidence = .8)
            
        if prayOrbI != None:
            prayOrbI = pyautogui.center(prayOrbI)
            print(f"Prayer orb Found.  [{ok}]")
            return prayOrbI, True
        elif prayOrbA != None:
            prayOrbA = pyautogui.center(prayOrbA)
            print(f"Prayer orb Found.  [{ok}]")
            return prayOrbA, False
        else:
            if tries < 5:
                print("\033[93m" + f"Error finding prayer orb, Trying again in {1+tries} seconds..." + "\033[0m")
                sleep(1+tries)
                tries += 1
                continue
            else:
                print("\033[91m" + f"Failed to find prayer orb after {tries} tries, disabling orb tracking" + "\033[0m")
                return False
                

def getMetro():
    tries = 0
    while True:
        try:
            metro = Metronomer(mcfg.windowName)
            metro.getMetronome()
            print(f"Metronome Found.   [{ok}]")
            return metro
        except Metronomer.CouldNotFind:
            if tries < 5:
                print("\033[93m" + f"Error finding Metronome, Trying again in {1+tries} seconds..." + "\033[0m")
                sleep(1+tries)
                tries += 1
                continue
            else:
                print("\033[91m" + f"Failed to find Metronome after {tries} tries, exiting" + "\033[0m")
                sleep(0.1)
                exit()
     

def main():
    global active
    firstClick = True
    toggle = True
    inside = True
    #Sets random delay for after gametick triggers
    Tar = copy.deepcopy(cfg.setTar)
    Tar += random.uniform(-cfg.tarVariance,cfg.tarVariance)
    clamp(Tar-cfg.tarVariance, Tar+cfg.tarVariance, Tar)
    #Get metronome and orb locations
    metro = getMetro()
    orbLoc, isInactive = getOrbLoc()
    print(f"Ready              [{ok}]")
    
    while True:   
        while active:
            mousePos = pyautogui.position()
            currentColour = getPixel(metro.x,metro.y)
                
            if math.dist(mousePos,orbLoc) >= cfg.disableRange and inside:
                print(f"Outside Orb        [{wait}]")
                inside = False
                
            if  math.dist(mousePos,orbLoc) <= cfg.disableRange and not inside:
                print(f"Inside Orb         [{ok}]")
                inside = True
                
            if currentColour in metro.colour[0] and inside and firstClick:
                if isInactive:
                    pyautogui.click()
                    sleep(.6)
                    firstClick = False
                else:
                    firstClick = False
            
            if  currentColour == metro.colour[0] and toggle and inside and not firstClick:
                sleep(randomDelay(cfg.minDelay,cfg.maxDelay,cfg.Dev,Tar,cfg.weighted))
                pyautogui.click(clicks=2, 
                                interval=randomDelay(cfg.flickMinDelay,cfg.flickMaxDelay,cfg.flickDev,cfg.flickTar,cfg.weighted))
                toggle = False
                    
            elif currentColour == metro.colour[1] and not toggle and inside and not firstClick:
                sleep(randomDelay(cfg.minDelay,cfg.maxDelay,cfg.Dev,Tar,cfg.weighted))
                pyautogui.click(clicks=2, 
                                interval=randomDelay(cfg.flickMinDelay,cfg.flickMaxDelay,cfg.flickDev,cfg.flickTar,cfg.weighted))
                toggle = True     
            
 
        else:
            print(f"Disabled           [{no}]")
            exit()      #Exits thread
            
#Triggers          
def activate():
    global active
    active ^= True
    if active:
        print(f"Enabling...        [{wait}]")
        t = threading.Thread(target=main)
        t.start()
        
def leave():
    global active
    active = False
    sleep(.1)
    exit()


if __name__ == "__main__":
    active = cfg.active
    print(f"Loaded             [{ok}]")
    with GlobalHotKeys({cfg.activeHotkey: activate, cfg.exitHotkey: leave}) as h:
        h.join()