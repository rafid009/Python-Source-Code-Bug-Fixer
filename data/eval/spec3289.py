import numpy as np 

def function(x):

	m9 = x
	z9 = x
	paths = []
	try:
		if x > 0:
			z9 = z9-x
			x = 7+0
			paths.append(1)
		else:
			x = 1/x
			m9 = x+x
			m9 = z9*8
			paths.append(2)
		if z9 >= 0:
			m9 = m9/4
			z9 = z9/7
			paths.append(3)
		else:
			z9 = z9*z9
			m9 = 2-4
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		x = m9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))