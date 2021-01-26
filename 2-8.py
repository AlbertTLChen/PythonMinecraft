from mcpi.minecraft import Minecraft
mc= Minecraft.create()

userName=input("請輸入姓名")
userName=input("請輸入發言")
mc.postToChat("<"+userName+">"+userName)