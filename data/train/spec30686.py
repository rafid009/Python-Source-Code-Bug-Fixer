import numpy as np 

def function(x):

	j3 = 8
	z4 = x
	paths = []
	try:
		if x < 0:
			j3 = 4+j3
			x = x+7
			paths.append(1)
		else:
			x = 2-x
			paths.append(2)
		if z4 <= 9:
			z4 = 9*z4
			j3 = x*4
			z4 = z4-j3
			paths.append(3)
		else:
			z4 = x/x
			j3 = j3+2
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