import numpy as np 

def function(x):

	k6 = 9
	z4 = 7
	paths = []
	try:
		if z4 <= 4:
			x = x-5
			z4 = z4+5
			paths.append(1)
		else:
			k6 = k6/3
			paths.append(2)
		if z4 <= 9:
			k6 = k6*2
			k6 = 5/k6
			paths.append(3)
		else:
			z4 = 9*z4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k6 = x**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))