#main
class MainConfig:
    #Locate on window, or by screen. 
    #Setting to False becomes more stable, however need to ensure OSRS is visible when running. 
    useWindow = False
    ## Change this to your RuneLite window title (might have username) if set useWindow = True
    windowName = "RuneLite"

#autoprayflick
class AutoPrayFlickConfig:
    #If resizing/moving window, disable and re-enable the script to reset positions
    #Hotkey, Examples:"<ctrl>+<alt>+a", "<shift>+<ctr>+`". 
    #See https://cherrytree.at/misc/vk.htm for special keys Example: <112> for F1
    activeHotkey = "<112>"
    exitHotkey = "<ctrl>+c"
    
    #Start already activated
    active = False
    #Size of orb area, 25 should be perfect
    disableRange = 25       
    
    ##Random Distribtions##
    #If distrubtions should be weighted
    weighted = True     
    #Delay between flicks, in ms
    flickMinDelay = 85
    flickMaxDelay = 110
    flickDev = 2
    flickTar = 95
    #Delay between ticks, in ms
    minDelay = 0
    maxDelay = 200
    Dev = 10
    setTar = 75
    #randomises the target each start/stop (+- setTar's value)
    tarVariance = 30    