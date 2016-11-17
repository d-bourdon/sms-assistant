#!/bin/bash
str=$SMS_1_TEXT
tlf=$SMS_1_NUMBER
tlft=${tlf:0:3}			#on recupere le code pays
if test $tlft = "+33"; then	#on verifie que c'est un numero francais
	tlf=${tlf:3} 		#retrait du code pays (+33)
else
	exit
fi
if test "$str" = "Delivered"; then	#protection contre boucle infini de gammu
    exit
fi

sudo /usr/bin/python3 /home/pi/sms/main.py "$str" "$tlf"
exit
EOF
