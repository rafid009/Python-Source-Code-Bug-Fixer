import numpy as np 

def function(x):

	z4 = 5
	r6 = x
	paths = []
	try:
		if x <= 4:
			r6 = r6+9
			z4 = x*2
			z4 = x*9
			paths.append(1)
		else:
			x = 4-x
			paths.append(2)
		if z4 < 1:
			z4 = r6+9
			z4 = 4+z4
			z4 = 7+9
			paths.append(3)
		else:
			x = x/r6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r6 = x**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))