from mcpi.minecraft import Minecraft
mc= Minecraft.create()
x,y,z= mc.player.getTilePos()

x,y,z= mc.player.getTilePos()
try:
    answer=int(input('請問你右邊要放甚麼方塊:'))
    mc.setBlock(x+1,y,z,answer)
except:
    print('只能輸入數字!!!!!!!')

