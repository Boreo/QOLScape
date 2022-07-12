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

from time import sleep, time
from pynput.keyboard import GlobalHotKeys
from sys import exit, stdout
from modules.metronome import Metronomer
from modules.randomdistribution import randomDelay, clamp
from modules.pixelcolour import getPixel
from config import AutoPrayFlickConfig as cfg
from colorama import init, Fore
import random, math, threading, copy, pyautogui

#Pretty output
init(convert=True)
no = (Fore.RED + "X" + Fore.WHITE)
ok = (Fore.GREEN + "X" + Fore.WHITE)
wait = (Fore.LIGHTYELLOW_EX + "x" + Fore.WHITE)


def getOrb():
    #TODO: Might be better as object and allow to grab just whether orb is active or inactive.
    timeout = time() + 5
    notify = False 
    while True:
        prayOrbI = pyautogui.locateOnScreen(".\\resources\\prayerBInactive.png", confidence = .8)
        prayOrbA = pyautogui.locateOnScreen(".\\resources\\prayerBActive.png", confidence = .8)
            
        if prayOrbI != None:
            prayOrbI = pyautogui.center(prayOrbI)
            if notify:
                print(f"Pray Orb Found     [{ok}]")
            return prayOrbI, True
        elif prayOrbA != None:
            prayOrbA = pyautogui.center(prayOrbA)
            if notify:
                print(f"Pray Orb Found     [{ok}]")
            return prayOrbA, False
        else:
            if time() > timeout:
                print(Fore.RED + "Failed to find Prayer Orb after 5 seconds, disabling orb tracking" + Fore.WHITE)
                return False
            else:
                print(Fore.LIGHTYELLOW_EX + "Finding Pray Orb..." + Fore.WHITE)
                notify = True
                continue
                

def updateMetroLoc():
    global metro
    timeout = time() + 5
    while True:
        try:
            return metro.getMetronome(onlyLoc = True)
        except Metronomer.CouldNotFind:
            if time() > timeout:
                print(Fore.RED + "Failed to find Metronome after 5 seconds, exiting." + Fore.WHITE, end="\r")
                sleep(.1)
                exit()
            else:
                print(Fore.LIGHTYELLOW_EX + "Finding Metronome..." + Fore.WHITE)
                continue
            

def getMetro():
    timeout = time() + 5
    while True:
        try:
            metro = Metronomer()
            metro.getMetronome()
            print(f"Metronome Found    [{ok}]")
            return metro
        except Metronomer.CouldNotFind:
            if time() > timeout:
                print(Fore.RED + "Failed to find Metronome after 5 seconds, exiting." + Fore.WHITE)
                sleep(.1)
                exit()
            else:
                print(Fore.LIGHTYELLOW_EX + "Finding Metronome..." + Fore.WHITE)
                continue
     

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
    updateMetroLoc()
    orbLoc, isInactive = getOrb()
    print(f"Ready              [{ok}]")
    
    while True:   
        while active:
            mousePos = pyautogui.position()
            currentColour = getPixel(metro.x,metro.y)
                
            if math.dist(mousePos,orbLoc) >= cfg.disableRange and inside:
                print(f"Outside Orb        [{wait}]")
                inside = False
                firstClick = True
                orbLoc, isInactive = getOrb()
                
            if  math.dist(mousePos,orbLoc) <= cfg.disableRange and not inside:
                print(f"Inside Orb         [{ok}]")
                inside = True
                
            if currentColour in metro.colour[0] and inside and firstClick:
                if isInactive:
                    pyautogui.click()
                    firstClick = False
                else:
                    firstClick = False
                #Waits a tick to avoid spazzing out.
                if currentColour == metro.colour[0]:
                    toggle = False
                else:
                    toggle = True
            
            if  currentColour == metro.colour[0] and inside and toggle and not firstClick:
                sleep(randomDelay(cfg.minDelay,cfg.maxDelay,cfg.Dev,Tar,cfg.weighted))
                pyautogui.click(clicks=2, 
                                interval=randomDelay(cfg.flickMinDelay,cfg.flickMaxDelay,cfg.flickDev,cfg.flickTar,cfg.weighted))
                toggle = False
                    
            elif currentColour == metro.colour[1] and inside and not toggle and not firstClick:
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
    metro = getMetro()
    print(f"Loaded             [{ok}]")
    with GlobalHotKeys({cfg.activeHotkey: activate, cfg.exitHotkey: leave}) as h:
        h.join()