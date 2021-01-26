from mcpi.minecraft import Minecraft
mc= Minecraft.create()
import random

while True:
    x= mc.player.getTilePos()
    
    color=random.randrange(0,7)
   mc.player.getTilePos()Block(x,46,color)
    
    