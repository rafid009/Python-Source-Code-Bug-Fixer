import numpy as np 

def function(x):

	i5 = 7
	h4 = 3
	paths = []
	try:
		if x < 0:
			h4 = h4*x
			paths.append(1)
		else:
			i5 = i5+0
			x = 7-h4
			paths.append(2)
		if i5 < 7:
			h4 = 8/4
			paths.append(3)
		else:
			x = x-7
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		x = h4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))