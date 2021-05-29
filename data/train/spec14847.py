import numpy as np 

def function(x):

	z4 = 7
	u3 = x
	paths = []
	try:
		if x >= 2:
			x = x*z4
			x = 4*x
			u3 = u3+7
			paths.append(1)
		else:
			x = x/5
			z4 = 3/x
			paths.append(2)
		if x < 6:
			x = x/7
			paths.append(3)
		else:
			z4 = z4*5
			u3 = u3*4
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		x = u3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))