import numpy as np 

def function(x):

	i4 = 0
	z7 = x
	paths = []
	try:
		if z7 <= 5:
			z7 = 3+z7
			x = x/2
			x = 8*x
			paths.append(1)
		else:
			z7 = 2-8
			paths.append(2)
		if z7 < 9:
			x = 7+x
			i4 = i4/1
			i4 = x+z7
			paths.append(3)
		else:
			i4 = 9*z7
			z7 = x/z7
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		i4 = z7**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))