import serial
import errno
from colorama import Fore, Back, Style
from time import sleep
import files.var.globalVar as globalVar

global comSUCP2102
comSUCP2102 = '/dev/ttyUSB0'

def openportSUCP2102():
    global comportSUCP2102
    try:
        comportSUCP2102 = serial.Serial(port=comSUCP2102, baudrate=110, timeout=2, stopbits=serial.STOPBITS_ONE)
    except serial.SerialException as e:
        logging.error("Error during open port MeterWT210: %s" % e)

def closeportSUCP2102():
    global comportSUCP2102
    comportSUCP2102.close()

def sendDataSUCP2102(param1):
    openportSUCP2102()
    global comportSUCP2102
    try:
        comportSUCP2102.write(param1.encode())
        comportSUCP2102.write(b'\r\n')
    except serial.SerialException as e:
        logging.error("Error during read data MeterWT210: %s" % e)
    closeportSUCP2102()

def readDataSUCP2102():
    openportSUCP2102()
    global comportSUCP2102
    try:
        while True:
            data = comportSUCP2102.read()
            print(data.decode())
    except serial.SerialException as e:
        logging.error("Error during read data MeterWT210: %s" % e)
    closeportSUCP2102()