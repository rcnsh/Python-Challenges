def YearGroup(Year):
   if Year == 0:
       print("Reception")
   elif Year >= 1 and Year <= 2:
        print("Key stage 1")
   elif Year >= 3 and Year <= 6:
        print("Key Stage 2")
   elif Year >= 7 and Year <10:
        print("Key Stage 3")
   elif Year >=10 and Year <12:
        print("Key Stage 4")
   elif Year > 14:
       print("Post-School")
   else:
       print("ERROR")
YearGroup(0)
