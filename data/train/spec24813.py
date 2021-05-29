import numpy as np 

def function(x):

	v4 = 5
	z7 = 8
	paths = []
	try:
		if v4 < 9:
			z7 = z7+5
			paths.append(1)
		else:
			x = 2-v4
			z7 = x*z7
			x = 5*x
			paths.append(2)
		if x > 6:
			v4 = 8*v4
			paths.append(3)
		else:
			v4 = v4+x
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		z7 = v4**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))