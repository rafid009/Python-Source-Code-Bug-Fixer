import numpy as np 

def function(x):

	j8 = 5
	a3 = 6
	paths = []
	try:
		if a3 > 6:
			x = a3/x
			a3 = a3+3
			paths.append(1)
		else:
			a3 = a3-x
			j8 = 5+a3
			paths.append(2)
		if a3 > 5:
			j8 = x-7
			a3 = a3+2
			paths.append(3)
		else:
			x = 3-x
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		x = a3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))