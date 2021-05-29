import numpy as np 

def function(x):

	j9 = 5
	z5 = x
	paths = []
	try:
		if x <= 1:
			j9 = 3+3
			z5 = z5-3
			x = x+4
			paths.append(1)
		else:
			z5 = 0-j9
			x = 9+2
			paths.append(2)
		if x < 0:
			j9 = x+0
			j9 = 6+j9
			x = x*1
			paths.append(3)
		else:
			j9 = x*j9
			z5 = z5-j9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j9 = x**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))