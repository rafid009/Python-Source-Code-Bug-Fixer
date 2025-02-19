import numpy as np 

def function(x):

	u3 = 9
	z5 = x
	paths = []
	try:
		if u3 > 7:
			x = x/3
			z5 = z5*5
			paths.append(1)
		else:
			x = x-8
			paths.append(2)
		if u3 <= 8:
			u3 = 5-u3
			z5 = z5+z5
			paths.append(3)
		else:
			u3 = x+0
			u3 = u3-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u3 = x**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))