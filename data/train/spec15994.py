import numpy as np 

def function(x):

	z1 = 4
	m3 = 3
	paths = []
	try:
		if x > 6:
			x = z1-m3
			m3 = x/5
			m3 = m3*m3
			paths.append(1)
		else:
			m3 = 1+5
			paths.append(2)
		if m3 <= 2:
			x = 4*7
			x = 2/z1
			z1 = z1+1
			paths.append(3)
		else:
			z1 = z1+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z1 = x**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))