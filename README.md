# 3D-Spatial-Mapping-Device

The 3D Spatial Mapping device is an embedded system which creates a 3D representation of the environment in which the system is situated in. There are various components of this embedded system including the SimpleLink MSP432E401Y microcontroller, ToF sensor (VL43L1X), MOT-28BYJ48 stepper motor, push-button, and PC data processing.

The languages used to process the data achieved through I2C and UART sertial communication is Python. The libraries used are Open3d, PySerial, and NumPy. More information about this project is availible in a data sheet created for this device named 3D Spatial Mapping Device Data Sheet.pdf. 

# Device Setup 

The following diagram shows you how to setup up the hardware of the device: 

![Screen Shot 2021-10-21 at 7 46 00 PM](https://user-images.githubusercontent.com/70975819/138372056-01fb7924-d06f-4524-9130-4a4a71deaf92.png)

Next you will have to download the Keil IDE to run the C file for the microcontroller. Along with downloading Keil you will also have to download the PySerial library, Numpy, and the Open3d library in the latest version of Python. 


# Collecting Data

To collect data, you can just download the Keil folder and open the Keil project, which is for the microcontroller. Then you will have to open the Data_xyz.py file availible in the Python folder. To collect data you run the Keil Project and Data_xyz.py. Now all you have to do is press the push button to collect data. Every time the stepper motor completes a 360 degree turn, you displace the stepper motor by 1 cm to collect the next sample. Once you displace the stepper motor 10 times, you should have 10 sets of xyz measurements. The file with the measurements will automatically be saved in a .xyz file once you collected all samples. 

Here is a demo of collecting the data: 


Now all you do is run Open3d.py to see the 3d mapped environment around the device. Since I placed the device in a shoe box, I was able to get the following output. 

<img width="797" alt="Screen Shot 2021-10-21 at 8 02 18 PM" src="https://user-images.githubusercontent.com/70975819/138372874-0568828b-5645-4060-9067-b779c5098113.png">


