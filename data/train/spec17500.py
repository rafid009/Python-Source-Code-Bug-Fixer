import numpy as np 

def function(x):

	z7 = x
	i7 = 3
	x = 5
	paths = []
	try:
		if i7 > 9:
			x = x-3
			i7 = 2/8
			paths.append(1)
		else:
			z7 = z7/4
			x = 8/x
			x = x*6
			paths.append(2)
		if x <= 6:
			i7 = i7+6
			i7 = 2-i7
			paths.append(3)
		else:
			x = x-i7
			i7 = i7+i7
			x = x*x
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		x = z7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))