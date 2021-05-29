import numpy as np 

def function(x):

	z8 = 3
	v9 = x
	x = x
	paths = []
	try:
		if x < 5:
			z8 = z8+x
			paths.append(1)
		else:
			x = 5/2
			paths.append(2)
		if v9 > 5:
			v9 = 5/6
			z8 = 6*v9
			paths.append(3)
		else:
			x = x/1
			z8 = 8-z8
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		z8 = v9**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))