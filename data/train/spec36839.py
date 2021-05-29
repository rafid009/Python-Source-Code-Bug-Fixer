import numpy as np 

def function(x):

	v1 = 5
	z7 = x
	paths = []
	try:
		if v1 >= 1:
			z7 = z7*z7
			paths.append(1)
		else:
			z7 = z7-v1
			paths.append(2)
		if z7 > 2:
			x = x/x
			x = 4-9
			paths.append(3)
		else:
			v1 = x/7
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		x = v1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))