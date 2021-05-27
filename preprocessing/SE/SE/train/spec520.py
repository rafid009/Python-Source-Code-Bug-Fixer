import numpy as np 

def function(x):

	j5 = 4
	z8 = x
	paths = []
	try:
		if j5 >= 4:
			j5 = j5+6
			j5 = 5*1
			paths.append(1)
		else:
			j5 = z8+x
			paths.append(2)
		if z8 <= 2:
			j5 = j5-2
			paths.append(3)
		else:
			z8 = 8+3
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		z8 = z8**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))