import numpy as np 

def function(x):

	u7 = 3
	z4 = 7
	paths = []
	try:
		if z4 > 2:
			z4 = x+1
			x = x+5
			paths.append(1)
		else:
			u7 = u7/4
			x = z4/x
			u7 = 4/x
			paths.append(2)
		if x <= 9:
			x = x*z4
			paths.append(3)
		else:
			z4 = 7/3
			z4 = z4*8
			x = 2*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u7 = x**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))