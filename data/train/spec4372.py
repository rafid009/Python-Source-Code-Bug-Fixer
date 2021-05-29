import numpy as np 

def function(x):

	u3 = 5
	z6 = 9
	paths = []
	try:
		if u3 < 0:
			u3 = 5-2
			x = u3+x
			x = 1+x
			paths.append(1)
		else:
			x = x+u3
			paths.append(2)
		if z6 <= 1:
			u3 = 6+u3
			z6 = z6-2
			paths.append(3)
		else:
			z6 = 2/z6
			z6 = z6/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z6 = x**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))