import numpy as np 

def function(x):

	m1 = 6
	z4 = x
	paths = []
	try:
		if m1 > 9:
			m1 = x-m1
			paths.append(1)
		else:
			z4 = z4*3
			paths.append(2)
		if z4 >= 9:
			m1 = m1*z4
			m1 = m1+7
			m1 = 2*m1
			paths.append(3)
		else:
			z4 = m1-z4
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		x = z4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))