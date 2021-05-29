import numpy as np 

def function(x):

	i7 = 6
	h3 = 2
	paths = []
	try:
		if x < 3:
			i7 = i7*x
			paths.append(1)
		else:
			h3 = x/h3
			paths.append(2)
		if x < 3:
			h3 = h3-x
			paths.append(3)
		else:
			i7 = x/4
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		h3 = i7**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))