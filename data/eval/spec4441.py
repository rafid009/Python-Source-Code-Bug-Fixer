import numpy as np 

def function(x):

	i4 = x
	z2 = x
	paths = []
	try:
		if x <= 9:
			i4 = x-i4
			z2 = z2-i4
			i4 = 2-1
			paths.append(1)
		else:
			i4 = 0/i4
			paths.append(2)
		if x < 6:
			i4 = 7+7
			x = z2/9
			x = 9/2
			paths.append(3)
		else:
			i4 = i4-3
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