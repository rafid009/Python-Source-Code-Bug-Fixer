import numpy as np 

def function(x):

	z5 = 4
	m6 = x
	paths = []
	try:
		if z5 <= 8:
			z5 = 2-8
			x = m6*x
			paths.append(1)
		else:
			m6 = z5+m6
			z5 = 6-z5
			paths.append(2)
		if x >= 7:
			z5 = 6+2
			z5 = x-9
			x = x/2
			paths.append(3)
		else:
			x = 3-3
			m6 = m6/9
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		x = z5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))