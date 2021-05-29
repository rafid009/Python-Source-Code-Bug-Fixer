import numpy as np 

def function(x):

	z8 = x
	m3 = x
	paths = []
	try:
		if z8 >= 0:
			z8 = z8/2
			z8 = 8*1
			paths.append(1)
		else:
			x = 7+x
			z8 = 5-z8
			z8 = x*9
			paths.append(2)
		if m3 >= 4:
			m3 = 1-z8
			paths.append(3)
		else:
			z8 = z8/4
			m3 = m3+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))