import numpy as np 

def function(x):

	e9 = x
	z4 = x
	x = 2
	paths = []
	try:
		if x > 2:
			x = x*e9
			paths.append(1)
		else:
			e9 = e9+5
			x = x/x
			e9 = x-2
			paths.append(2)
		if e9 > 1:
			x = 4+x
			paths.append(3)
		else:
			x = x+x
			z4 = x/2
			x = x/6
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		x = e9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))