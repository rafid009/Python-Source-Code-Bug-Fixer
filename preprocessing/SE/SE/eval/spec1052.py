import numpy as np 

def function(x):

	z0 = 9
	m1 = x
	paths = []
	try:
		if x > 3:
			x = 0/4
			x = x+6
			paths.append(1)
		else:
			z0 = 1-z0
			x = 7-x
			x = x/8
			paths.append(2)
		if x >= 3:
			x = x-1
			x = x-m1
			m1 = m1+7
			paths.append(3)
		else:
			z0 = m1-1
			m1 = z0+m1
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		z0 = m1**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))