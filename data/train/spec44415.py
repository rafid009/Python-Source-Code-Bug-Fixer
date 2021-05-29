import numpy as np 

def function(x):

	m3 = x
	z4 = x
	paths = []
	try:
		if x < 1:
			z4 = 3-z4
			z4 = 3+x
			paths.append(1)
		else:
			m3 = x-m3
			z4 = 2+6
			x = m3/1
			paths.append(2)
		if x <= 1:
			x = z4*7
			paths.append(3)
		else:
			z4 = z4+5
			m3 = 3/m3
			m3 = x-z4
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