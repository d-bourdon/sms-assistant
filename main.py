#!/usr/bin/python3
import os, sys, subprocess
from subprocess import Popen, PIPE, call
from config import config
#from subprocess import call


# check des erreurs fatal
argc = len(sys.argv)
if argc != 3:
	sys.exit(1)

#Definition des variables
retour = "error"
cmd = "none"
i = 0
message = sys.argv[1]
tel = sys.argv[2]

if ((message == "ip" or message == "Ip") and (tel == config["tel_admin"])):
	cmd = "monip"
elif (message == "reboot" or message == "Reboot") and tel == config["tel_admin"]:
	cmd = "reboot"
else:
	message = "Hello World";
# Si on as une commande a executer, on recupere le retour dans message
if cmd != "none":
	proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
	message = proc.stdout.read()
	#message = Popen(cmd, shell=True, bufsize=20, stdout=PIPE).stdout

if message != '' and message != "error":
	call(["gammu-smsd-inject", "TEXT", tel, "-text", message]);
