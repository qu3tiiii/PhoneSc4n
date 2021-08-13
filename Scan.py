import time
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from colorama import *
print(Fore.MAGENTA+"""
        .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'   DIE    `98v8P'  DIE    `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '
============================================================|
                        Number-Scanner By Qu3ti!            |
                        https://github.com/qu3tiiii         |
============================================================|
""")
print (Fore.LIGHTMAGENTA_EX+"Ingresa el numero: ")
data=input()
Num=phonenumbers.parse(data)
xd=(Fore.GREEN+"Pais: "+geocoder.description_for_number (Num , "en"))
x=("Carrier: "+carrier.name_for_number (Num , "en"))
       ################## 
        #                # 
        #                # 
        # Que haces      # 
        # Leyendo mi     #
        # Codigo?        # 
        # JAJAJAJA       # 
        #                # 
        #                # 
        ################## 
time.sleep(0.3)
print(xd)
print(x)
time.sleep(15)
quit
        ################## 
        #                # 
        #                # 
        # Que haces      # 
        # Leyendo mi     #
        # Codigo?        # 
        # JAJAJAJA       # 
        #                # 
        #                # 
        ################## 
