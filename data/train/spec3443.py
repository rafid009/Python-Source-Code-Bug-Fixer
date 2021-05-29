import numpy as np 

def function(x):

	z7 = 8
	u3 = x
	paths = []
	try:
		if x >= 5:
			x = x-x
			x = 5*x
			paths.append(1)
		else:
			z7 = z7*7
			u3 = u3*7
			paths.append(2)
		if x <= 9:
			u3 = u3-1
			z7 = z7+5
			x = u3+1
			paths.append(3)
		else:
			x = 5+8
			z7 = 3+z7
			z7 = 4*4
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		u3 = u3**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))