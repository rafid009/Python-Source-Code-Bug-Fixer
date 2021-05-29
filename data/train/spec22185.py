import numpy as np 

def function(x):

	z2 = x
	m0 = 8
	paths = []
	try:
		if m0 > 9:
			m0 = m0+8
			paths.append(1)
		else:
			m0 = 4-m0
			m0 = 0-7
			paths.append(2)
		if m0 <= 3:
			x = x/x
			z2 = 4-6
			paths.append(3)
		else:
			x = x*2
			x = z2*x
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		z2 = m0**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))