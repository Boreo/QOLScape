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



import win32gui

dc = win32gui.GetWindowDC(0)

def getPixel(x,y):
    """Outputs pixel colour from X Y screen coords and returns Runelite compatible ARGB hex code.

    Args:
        x int: X coordinate of pixel
        y int: X coordinate of pixel

    Returns:
        str: RuneLite compatable ARGB hex code (ffrrggbb) alpha should always be ff
    """
    colorRef = win32gui.GetPixel(dc, x, y)
    red = colorRef % 256
    colorRef //= 256
    green = colorRef % 256
    colorRef //= 256
    blue = colorRef
    #print(f"{red} {green} {blue}")
    return (f"ff{red:02x}{green:02x}{blue:02x}")