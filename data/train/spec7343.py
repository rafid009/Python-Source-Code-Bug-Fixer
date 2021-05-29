import numpy as np 

def function(x):

	z6 = 3
	r7 = 6
	paths = []
	try:
		if r7 > 4:
			r7 = z6-3
			paths.append(1)
		else:
			z6 = 4+r7
			paths.append(2)
		if x >= 7:
			r7 = z6+2
			x = 8-x
			paths.append(3)
		else:
			x = x/4
			r7 = r7+9
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