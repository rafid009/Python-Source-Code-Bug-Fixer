import numpy as np 

def function(x):

	z7 = x
	u2 = 9
	paths = []
	try:
		if z7 <= 4:
			u2 = 2-5
			x = x/3
			z7 = 1-z7
			paths.append(1)
		else:
			x = x*6
			u2 = z7+5
			u2 = z7+1
			paths.append(2)
		if u2 >= 8:
			z7 = z7+3
			x = x+3
			paths.append(3)
		else:
			z7 = x/3
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		x = u2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))