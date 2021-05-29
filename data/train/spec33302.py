import numpy as np 

def function(x):

	z2 = x
	j5 = x
	x = x
	paths = []
	try:
		if z2 <= 5:
			x = 6/x
			j5 = 6*z2
			x = x+3
			paths.append(1)
		else:
			z2 = 9*z2
			j5 = 4/9
			paths.append(2)
		if z2 >= 3:
			j5 = 1*x
			paths.append(3)
		else:
			z2 = z2-6
			j5 = x-7
			z2 = 3/z2
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		z2 = j5**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))