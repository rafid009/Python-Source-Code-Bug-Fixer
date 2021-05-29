import numpy as np 

def function(x):

	r6 = 1
	z6 = 5
	paths = []
	try:
		if z6 <= 5:
			z6 = 0-z6
			paths.append(1)
		else:
			z6 = z6+r6
			r6 = 4+9
			paths.append(2)
		if r6 >= 3:
			x = 5*x
			r6 = r6+z6
			z6 = z6*0
			paths.append(3)
		else:
			z6 = r6/z6
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