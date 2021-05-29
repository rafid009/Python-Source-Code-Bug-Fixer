import numpy as np 

def function(x):

	j8 = 4
	z1 = 7
	paths = []
	try:
		if z1 >= 8:
			x = j8-x
			paths.append(1)
		else:
			j8 = j8*4
			j8 = 4-9
			paths.append(2)
		if z1 < 7:
			z1 = 3*z1
			paths.append(3)
		else:
			x = 9/x
			z1 = z1/z1
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		j8 = j8**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))