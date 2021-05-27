import numpy as np 

def function(x):

	m8 = 4
	k4 = x
	paths = []
	try:
		if m8 > 1:
			m8 = 5*2
			m8 = 9-0
			m8 = m8/x
			paths.append(1)
		else:
			k4 = 7-k4
			paths.append(2)
		if m8 < 9:
			k4 = k4/5
			m8 = m8+8
			paths.append(3)
		else:
			k4 = m8*k4
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		m8 = k4**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))