import time
i=1
while True:
   t=time.gmtime ()
   a=time.strftime("%I:%M:%S",t)
   print("\r{}".format(a),end="")
   time.sleep(1)
