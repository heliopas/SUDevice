import serial
import errno
from colorama import Fore, Back, Style
from time import sleep
import files.var.globalVar as globalVar

global comMeterWT210
comMeterWT210 = globalVar.comPORT

def openportMeterWT210():
    global comportMeterWT210
    try:
        comportMeterWT210 = serial.Serial(port=comMeterWT210, baudrate=9600, timeout=2, stopbits=serial.STOPBITS_ONE)
    except serial.SerialException as e:
        logging.error("Error during open port MeterWT210: %s" % e)

def closeportMeterWT210():
    global comportMeterWT210
    comportMeterWT210.close()

def sedDataReadMeterWT210(param1):
    openportMeterWT210()
    global comportMeterWT210
    try:
        comportMeterWT210.write(param1.encode())
        comportMeterWT210.write(b'\r\n')
    except serial.SerialException as e:
        logging.error("Error during read data MeterWT210: %s" % e)
    closeportMeterWT210()