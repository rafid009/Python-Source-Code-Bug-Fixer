import numpy as np 

def function(x):

	m1 = x
	z8 = 1
	paths = []
	try:
		if z8 > 1:
			m1 = 3/1
			m1 = m1/9
			paths.append(1)
		else:
			x = 5+x
			m1 = 5/x
			paths.append(2)
		if x > 1:
			m1 = m1/3
			z8 = z8*8
			paths.append(3)
		else:
			z8 = x+8
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		x = z8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))