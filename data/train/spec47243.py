import numpy as np 

def function(x):

	z4 = 2
	m3 = 8
	paths = []
	try:
		if m3 < 2:
			x = 7+m3
			paths.append(1)
		else:
			m3 = 0+m3
			x = x-z4
			paths.append(2)
		if z4 >= 6:
			m3 = 1*m3
			paths.append(3)
		else:
			z4 = z4-5
			x = x-m3
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		m3 = z4**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))