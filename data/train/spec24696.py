import numpy as np 

def function(x):

	z2 = x
	m5 = 1
	paths = []
	try:
		if m5 < 2:
			x = 9-x
			x = 8*x
			paths.append(1)
		else:
			m5 = z2*m5
			x = x-8
			paths.append(2)
		if z2 < 0:
			x = z2-x
			m5 = m5/4
			m5 = 4+3
			paths.append(3)
		else:
			z2 = z2*z2
			z2 = m5*7
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		z2 = z2**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))