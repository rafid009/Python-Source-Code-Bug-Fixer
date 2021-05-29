import numpy as np 

def function(x):

	z7 = x
	i5 = 3
	paths = []
	try:
		if i5 < 7:
			i5 = z7+2
			paths.append(1)
		else:
			z7 = z7+x
			paths.append(2)
		if z7 > 3:
			z7 = i5/7
			i5 = 4/i5
			paths.append(3)
		else:
			x = x+x
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		z7 = i5**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))