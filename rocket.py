import numpy as np

class Rocket:
	def __init__(self):
		self.b = 0.2
		self.h = 2

		self.l = 1

		self.k = 3000

		self.u = np.array(([[0, 0]]))
		self.t = np.array(([0]))

		self.o = True

	def dxdt(self, t, x):
		dx = np.zeros_like(x)

		u = self.compute_inputs(t, x)
		G = 6.67408e-11
		m_e = 5.972e24
		r_e = 6.371e6

		m = x[6]

		T = 0
		p = 0

		h = (x[2]**2 + x[4]**2)**.5 - r_e

		if h < 11000:
			T = 15.04 - 0.00649*h
			p = 101.29*((T+273.1)/288.08)**5.256
		elif h < 25000:
			T = -56.54
			p = 22.65*np.e**(1.73-0.000157*h)
		else:
			T = -131.21 + 0.00299*h
			p = 2.488*((T+273.1)/216.6)**-11.388

		rho = p/(0.2869 * (T+273.1))

		I = 12.0*self.l/((self.h**2 + self.b**2))
		D = 0.5*rho*np.sqrt(x[3]**2 + x[5]**2)*1*(self.b/2)**2*np.pi*20
		g = G*m_e/((x[2]**2 + x[4]**2)**1.5)

		dx[0] = x[1];
		dx[1] = I/m*u[0,0] - x[1]/m*u[0,1];
		dx[2] = x[3];
		dx[3] = np.cos(x[0])/m*u[0,0] - g*x[2] - (x[3] + np.sin(x[0])*self.k)/m*u[0,1] - D*x[3]/m
		dx[4] = x[5];
		dx[5] = np.sin(x[0])/m*u[0,0] - g*x[4] - (x[5] - np.cos(x[0])*self.k)/m*u[0,1] - D*x[5]/m
		dx[6] = - 0.001*u[0,1];

		if (x[2]**2 + x[4]**2)**.5 < r_e:
			dx[0] = 0
			dx[1] = 0
			dx[2] = 0
			dx[3] = 0
			dx[4] = 0
			dx[5] = 0

		return dx

	def compute_inputs(self, t, x):
		u = np.zeros((1, 2))

		angle = np.pi/2 + np.arctan2(x[2], x[4])

		u[0,0] = (0.05*(-x[0] - angle) -1.2*x[1])*0.0015

		r_e = 6.371e6
		if (x[2]**2 + x[4]**2)**.5 < r_e + 35.786e6 and self.o:
			u[0, 1] = 1
		else:
			self.o = False

		return u