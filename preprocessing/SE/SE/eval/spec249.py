import numpy as np 

def function(x):

	z7 = x
	i8 = x
	paths = []
	try:
		if i8 <= 1:
			z7 = 9-z7
			x = 4-x
			paths.append(1)
		else:
			x = x*8
			z7 = 0*z7
			paths.append(2)
		if z7 > 3:
			i8 = i8-7
			i8 = i8+x
			paths.append(3)
		else:
			x = z7/5
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		x = i8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))