import numpy as np 

def function(x):

	j7 = x
	z0 = 9
	paths = []
	try:
		if z0 < 7:
			x = x/x
			x = x/j7
			paths.append(1)
		else:
			x = x+5
			j7 = 6-3
			paths.append(2)
		if z0 > 9:
			z0 = z0*2
			j7 = j7+0
			z0 = x*5
			paths.append(3)
		else:
			x = x*1
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