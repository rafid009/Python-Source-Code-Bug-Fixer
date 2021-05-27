import numpy as np 

def function(x):

	u9 = 2
	z4 = 1
	paths = []
	try:
		if x > 2:
			x = u9+x
			paths.append(1)
		else:
			z4 = 7*z4
			x = x+1
			u9 = x-6
			paths.append(2)
		if z4 > 1:
			u9 = 5+u9
			paths.append(3)
		else:
			x = 6+x
			z4 = 9-z4
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		x = u9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))