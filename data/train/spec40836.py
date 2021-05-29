import numpy as np 

def function(x):

	z9 = x
	m8 = 8
	paths = []
	try:
		if z9 > 2:
			x = x+x
			x = 4+x
			x = x/1
			paths.append(1)
		else:
			z9 = 0-x
			x = m8+z9
			m8 = 3+z9
			paths.append(2)
		if z9 < 1:
			x = 4*2
			paths.append(3)
		else:
			z9 = 9*z9
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		x = z9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))