import numpy as np 

def function(x):

	i6 = 8
	e0 = x
	paths = []
	try:
		if x >= 0:
			i6 = i6-e0
			x = 5+3
			paths.append(1)
		else:
			e0 = 8+e0
			paths.append(2)
		if x >= 9:
			x = 5*x
			e0 = e0/i6
			paths.append(3)
		else:
			e0 = i6/x
			i6 = x/i6
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		i6 = e0**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))