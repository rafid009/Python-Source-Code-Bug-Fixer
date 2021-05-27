import numpy as np 

def function(x):

	u3 = x
	z5 = x
	paths = []
	try:
		if z5 > 7:
			u3 = 2*x
			u3 = x/8
			x = x+0
			paths.append(1)
		else:
			u3 = z5*0
			x = x+z5
			u3 = 8+4
			paths.append(2)
		if u3 > 8:
			z5 = z5*x
			z5 = u3+z5
			z5 = 2*u3
			paths.append(3)
		else:
			z5 = z5/u3
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