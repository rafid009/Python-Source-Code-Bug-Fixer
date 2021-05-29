import numpy as np 

def function(x):

	m7 = 2
	z9 = 6
	paths = []
	try:
		if z9 > 7:
			z9 = 7-z9
			paths.append(1)
		else:
			m7 = z9*m7
			z9 = z9-7
			m7 = 1*2
			paths.append(2)
		if x <= 9:
			x = m7*x
			z9 = 7/z9
			paths.append(3)
		else:
			x = x+9
			m7 = m7/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z9 = x**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))