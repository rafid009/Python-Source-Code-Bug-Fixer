import numpy as np 

def function(x):

	i0 = x
	i1 = 9
	paths = []
	try:
		if i0 >= 6:
			x = 7/x
			i0 = i0-i0
			paths.append(1)
		else:
			x = 7/x
			i1 = x/6
			paths.append(2)
		if i1 < 9:
			i1 = x/8
			i1 = 2/9
			i1 = i1/6
			paths.append(3)
		else:
			x = x+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i0 = x**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))