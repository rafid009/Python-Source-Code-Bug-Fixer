import numpy as np 

def function(x):

	k0 = 5
	m0 = 8
	paths = []
	try:
		if x < 9:
			k0 = 9+k0
			k0 = k0/3
			paths.append(1)
		else:
			k0 = x/3
			paths.append(2)
		if m0 >= 3:
			x = 0+x
			paths.append(3)
		else:
			m0 = k0-m0
			m0 = m0*x
			k0 = x*k0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m0 = x**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))