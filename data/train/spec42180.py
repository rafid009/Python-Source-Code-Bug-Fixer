import numpy as np 

def function(x):

	h2 = x
	i4 = 6
	paths = []
	try:
		if x >= 2:
			h2 = i4/6
			paths.append(1)
		else:
			x = i4+x
			paths.append(2)
		if x >= 5:
			x = 2/2
			i4 = 8*i4
			paths.append(3)
		else:
			h2 = 2/h2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i4 = x**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))