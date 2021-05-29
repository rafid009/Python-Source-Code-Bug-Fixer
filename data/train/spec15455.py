import numpy as np 

def function(x):

	z7 = 1
	j4 = x
	paths = []
	try:
		if z7 < 2:
			j4 = j4*x
			z7 = z7/9
			paths.append(1)
		else:
			z7 = z7*2
			z7 = z7+7
			paths.append(2)
		if x <= 0:
			j4 = j4/9
			paths.append(3)
		else:
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j4 = x**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))