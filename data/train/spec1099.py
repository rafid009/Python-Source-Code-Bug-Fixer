import numpy as np 

def function(x):

	z4 = 1
	m7 = x
	paths = []
	try:
		if x <= 8:
			x = x+m7
			z4 = 4*z4
			m7 = 0-m7
			paths.append(1)
		else:
			m7 = m7*3
			m7 = m7-8
			z4 = z4*5
			paths.append(2)
		if m7 <= 0:
			z4 = m7*z4
			x = 8-8
			paths.append(3)
		else:
			x = 7-x
			m7 = 3-2
			m7 = 3*x
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