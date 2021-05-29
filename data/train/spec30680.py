import numpy as np 

def function(x):

	u3 = 6
	z2 = 0
	paths = []
	try:
		if u3 >= 2:
			u3 = 2*u3
			u3 = u3/2
			paths.append(1)
		else:
			u3 = u3/u3
			u3 = u3*7
			paths.append(2)
		if u3 <= 6:
			u3 = z2*1
			paths.append(3)
		else:
			u3 = u3*9
			z2 = z2*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z2 = x**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))