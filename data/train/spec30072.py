import numpy as np 

def function(x):

	k4 = 7
	m3 = x
	paths = []
	try:
		if m3 >= 8:
			m3 = m3*3
			x = 6-5
			paths.append(1)
		else:
			m3 = m3-5
			m3 = 0/m3
			k4 = 9+k4
			paths.append(2)
		if x >= 0:
			k4 = x-k4
			m3 = k4-9
			m3 = 3/m3
			paths.append(3)
		else:
			k4 = k4*m3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m3 = x**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))