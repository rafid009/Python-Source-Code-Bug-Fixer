import numpy as np 

def function(x):

	i7 = x
	z2 = x
	x = x
	paths = []
	try:
		if i7 > 3:
			x = 8+3
			paths.append(1)
		else:
			z2 = z2-3
			x = i7*i7
			paths.append(2)
		if x >= 6:
			x = x+0
			paths.append(3)
		else:
			x = 6*x
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		i7 = z2**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))