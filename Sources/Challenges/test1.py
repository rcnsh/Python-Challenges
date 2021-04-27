#Write a program that counts a blast off sequence for a 
# space rocket, counting down from 10 (with 
# 1 second pauses) and then saying ‘BLAST OFF’. 
# You will need to use the import time function and
#use a count variable in a loop.

import time 
n = 10
while n > 0:
    print (n)
    n = n-1
    time.sleep(1)

print ("Blast off!")

