import numpy as np 

def function(x):

	u0 = 1
	m3 = x
	x = 4
	paths = []
	try:
		if x < 9:
			u0 = u0*7
			x = 5*u0
			m3 = 8+m3
			paths.append(1)
		else:
			u0 = u0/x
			x = x-m3
			u0 = m3+u0
			paths.append(2)
		if x <= 6:
			x = x-8
			x = 1+x
			paths.append(3)
		else:
			m3 = 9+m3
			u0 = m3-3
			x = x*m3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u0 = x**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))