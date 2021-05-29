import numpy as np 

def function(x):

	h4 = x
	i4 = x
	x = x
	paths = []
	try:
		if i4 >= 6:
			h4 = 5-h4
			x = x+x
			paths.append(1)
		else:
			h4 = 2+h4
			paths.append(2)
		if x <= 3:
			h4 = 9-h4
			paths.append(3)
		else:
			h4 = h4*3
			i4 = i4-2
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		x = i4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))