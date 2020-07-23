import TR_CE_SRD_World

i = 1
while i < 10:

    w1 = TR_CE_SRD_World.World("Blerit")
    w1.genWorld()
    w1.printUWPString()
    i += 1