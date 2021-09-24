import serial
import math

#Diljot Dola Saini
#400252842
#dolasaid

serialpath = '/dev/tty.usbmodemME4010231'
s = serial.Serial(serialpath, 115200)

print("Opening: " + s.name)
s.write(b'1') #Half-duplex communication with microcontroller

#Initialize angle and x-direction distance 
ang = 0
xdis = 0
for i in range(10): #10 plane measurements in total 
    xdis = xdis + 100 #increase x distance by 1 cm each time 
    f = open('measurements.xyz', 'a')
    for j in range(64):
        a = s.readline()                #readbytes     
        dis = float(a.decode())         #convert bytes->str->float
        #Convert raw distance to y,z distance 
        ang = ang + 5.625               
        x = xdis
        y = dis*math.cos(math.pi*(ang/180))
        z = dis*math.sin(math.pi*(ang/180))
        x, y, z = map(float,(x, y, z))
        f.write("{}\t {}\t {}\n".format(x,y,z)) #write to file 
        print(dis)
    f.close()
    
print("Closing: " + s.name)
s.close(); #close after 10 planes of measurements 
