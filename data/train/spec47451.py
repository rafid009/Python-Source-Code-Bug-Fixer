import numpy as np 

def function(x):

	o0 = x
	z7 = 9
	paths = []
	try:
		if x > 2:
			z7 = 8-z7
			z7 = z7/5
			x = x-x
			paths.append(1)
		else:
			x = z7*x
			x = 7/x
			z7 = x-o0
			paths.append(2)
		if o0 > 3:
			x = x+z7
			x = x+1
			paths.append(3)
		else:
			x = x/1
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		x = o0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))