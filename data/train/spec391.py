import numpy as np 

def function(x):

	u7 = 8
	z8 = x
	x = x
	paths = []
	try:
		if x <= 7:
			x = 8-x
			u7 = u7*z8
			paths.append(1)
		else:
			u7 = 1/1
			paths.append(2)
		if x > 8:
			u7 = 2-u7
			paths.append(3)
		else:
			z8 = z8+0
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		u7 = z8**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))