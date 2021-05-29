import numpy as np 

def function(x):

	m2 = x
	z7 = 0
	paths = []
	try:
		if z7 < 9:
			x = 9*x
			x = x-5
			paths.append(1)
		else:
			m2 = m2/4
			x = x/5
			z7 = z7/4
			paths.append(2)
		if m2 < 5:
			z7 = 9+z7
			paths.append(3)
		else:
			z7 = z7-7
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		x = m2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))