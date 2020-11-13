# Started from Tello Template
# This Python app is in the Public domain
# Some parts from Tello3.py

import threading, socket, sys, time, subprocess

# GLOBAL VARIABLES DECLARED HERE....
host = ''
port = 9000
locaddr = (host, port)
tello_address = ('192.168.10.1', 8889)  # Get the Tello drone's address

# Creates a UDP socketd
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(locaddr)


def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print('\n****Keep Eye on Drone****\n')
            break


def sendmsg(msg, sleep=6):
    print("Sending: " + msg)
    msg = msg.encode(encoding="utf-8")
    sock.sendto(msg, tello_address)
    time.sleep(sleep)


# recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()


# CREATE FUNCTIONS HERE....

# Drone mission through first hoop
def hoop1():
    sendmsg("up 65")
    sendmsg("forward 170")


# Drone mission through second hoop
def hoop2():
    sendmsg("up 10")
    sendmsg("forward 180")


# Drone mission through third hoop
def hoop3():
    sendmsg("forward 50")
    sendmsg("ccw 90")
    sendmsg("forward 170")
    sendmsg("ccw 90")
    sendmsg("forward 230")


def hoop4():
    print("hi")


print("\nAlex Symanzik")
print("Program Name: Drone Flying Comp")
print("Date: 11/13/2020")
print("\n****CHECK YOUR TELLO WIFI ADDRESS****")
print("\n****CHECK SURROUNDING AREA BEFORE FLIGHT****")
ready = input('\nAre you ready to take flight: ')

try:
    if ready.lower() == 'yes' or ready.lower() == 'y':
        print("\nStarting Drone!\n")

        sendmsg('command', 0)
        sendmsg('takeoff')

        hoop1()
        hoop2()
        hoop3()
        # hoop4()

        sendmsg('land')

        print('\nGreat Flight!!!')

    else:
        print('\nMake sure you check WIFI, surroundings, co-pilot is ready, re-run program\n')
except KeyboardInterrupt:
    sendmsg('emergency')

breakr = True
sock.close()
