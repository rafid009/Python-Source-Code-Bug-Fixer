import numpy as np 

def function(x):

	z7 = x
	k5 = 3
	paths = []
	try:
		if x <= 2:
			k5 = k5-k5
			x = x+9
			k5 = k5-4
			paths.append(1)
		else:
			z7 = 9*z7
			x = z7/x
			paths.append(2)
		if k5 >= 5:
			k5 = 7+k5
			z7 = z7+4
			paths.append(3)
		else:
			x = x*3
			x = x+9
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		k5 = z7**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))