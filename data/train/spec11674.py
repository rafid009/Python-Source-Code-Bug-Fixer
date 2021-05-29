import numpy as np 

def function(x):

	m0 = 4
	o3 = 0
	paths = []
	try:
		if x >= 6:
			m0 = m0-m0
			m0 = m0+6
			paths.append(1)
		else:
			o3 = 2+m0
			m0 = m0*1
			paths.append(2)
		if x > 8:
			m0 = x-o3
			m0 = o3/6
			m0 = o3-o3
			paths.append(3)
		else:
			m0 = m0+m0
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