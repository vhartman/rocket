# Simulation of a starting/landing a rocket

## Purpose
Originally, I only wanted to compute the optimal control inputs for landing a rocket. The goal has since branched out to first starting a rocket optimally and getting it to orbit before actually landing it.

## Status
A preliminary model of the rocket is finished and produces more or less sensible results.
* Gravity: Earth reduced to a point mass, gravity coming from the center of the earth.
* Atmosphere: Density, pressure, and temperature model taken from [NASA](https://www.grc.nasa.gov/www/k-12/airplane/atmosmet.html)
* Aerodynamics/Drag: Currently reduced to the drag acting on a sphere
* Control input:
  * Unlimited action in lateral direction ("thrusters" that do not consume fuel)
  * Fuel consuming engine in longitudinal direction. Only positive input possible.
  
### Todo
* Better aerodynamic model
* Extend rocket to have a nose-cone: include center of pressure in the aerodynamic model
* Include Lift/Drag (lead to automatic stabilization of the rocket)
