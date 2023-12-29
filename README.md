# Greenhouse Control II (2018)

Environmental monitoring system:

* Temperature (ºC)
* Relative humidity (%)
* Atmospheric pressure kPa
* Light intensity (lux)

Its based on Raspberry PI/Linux with software developed in Python and remote control via cell phone application (Android Only). 

Development of all stages, electronics, assembly and software. 

The System also acts automatically to maintain environmental conditions within established limits (temperature and humidity) acting on:

* Ventilation system
* Fogger
* Irrigation

According to the plants' needs. it also learns from the manual actuation of the system (human actuation), so it will build a plant care model depending on environmental conditions and the time of year.

## The Hardware

Developed with Raspberry PI Zero, running Linux, controlls a relay module that acts on a power panel, it carries out all the environmental control of the greenhouse, maintaining the parameters for the acclimatization of young plants recently left the Biotechnology laboratory.

![image](https://github.com/alexandredrefahl/greenhouse-control-II/assets/24326296/e283c97a-6ff7-4d3d-9776-b120dd1d5aae)

## Android App

_(Not included in this repository)_

Through the application it is possible to monitor environmental conditions in addition to acting on the equipment remotely.

![image](https://github.com/alexandredrefahl/greenhouse-control-II/assets/24326296/2d4e0d7f-5a22-4602-bf36-390adaba8d21)

