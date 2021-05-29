import numpy as np 

def function(x):

	z4 = x
	j1 = x
	paths = []
	try:
		if j1 >= 1:
			z4 = z4+x
			paths.append(1)
		else:
			j1 = 5-3
			x = 2+x
			j1 = 1-z4
			paths.append(2)
		if j1 > 9:
			j1 = 6+5
			paths.append(3)
		else:
			x = z4*x
			x = x*3
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		j1 = z4**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))