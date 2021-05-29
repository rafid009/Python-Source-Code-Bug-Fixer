import numpy as np 

def function(x):

	n9 = 3
	i8 = 2
	paths = []
	try:
		if i8 <= 1:
			x = x*8
			x = x*x
			paths.append(1)
		else:
			n9 = 2*x
			paths.append(2)
		if i8 < 1:
			x = x*i8
			i8 = 2/i8
			paths.append(3)
		else:
			n9 = n9*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i8 = x**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))