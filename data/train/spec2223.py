import numpy as np 

def function(x):

	z2 = 6
	i8 = x
	paths = []
	try:
		if z2 <= 3:
			x = x-x
			paths.append(1)
		else:
			i8 = i8*i8
			z2 = z2/x
			x = x/1
			paths.append(2)
		if i8 > 5:
			x = x+5
			x = 1*9
			paths.append(3)
		else:
			z2 = x*x
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		z2 = z2**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))