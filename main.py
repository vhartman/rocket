import numpy as np
import matplotlib.pyplot as plt

import scipy.integrate as integrate
from scipy.integrate import ode

from rocket import *

if __name__ == "__main__":
	r = Rocket()
	r_e = 6.371e6

	y0 = [0.0, 0.00000, 0, 0, r_e, 0, 200]
	t1 = 100000

	# t = np.linspace(0, t1, 10000)
	# x = integrate.odeint(r.dxdt, y0, t)

	o = ode(r.dxdt)
	o.set_initial_value(y0, 0)

	t = [0]
	x = np.array([y0])

	dt = 10
	while o.successful() and o.t < t1 and (x[-1, 2]**2 + (x[-1, 4])**2)**.5 >= r_e:
		res = o.integrate(o.t+dt)
		res =  np.expand_dims(res, axis=1).T

		t = np.append(t, o.t+dt)
		x = np.append(x, res, axis=0)

	a = []
	b = []
	for angle in np.linspace(0, 2*np.pi, 1000):
		a.append(np.sin(angle))
		b.append(np.cos(angle))

	a = np.array(a)
	b = np.array(b)

	f, ax = plt.subplots(2, 2)
	ax[0,0].plot(x[:, 2], x[:, 4])
	ax[0,0].plot(a*r_e, b*r_e)
	ax[0,0].plot(a*(r_e + 35.786e6), b*(r_e + 35.786e6))

	ax[0,0].axis('equal')
	ax[1,0].plot(t, x[:, 3])
	ax[1,0].plot(t, x[:, 5])
	ax[0,1].plot(t, x[:, 0])
	ax[0,1].plot(t, x[:, 1])
	ax[1,1].plot(t, x[:, 6])
	plt.show()