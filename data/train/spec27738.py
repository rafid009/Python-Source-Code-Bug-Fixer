import numpy as np 

def function(x):

	i0 = 6
	h4 = 5
	paths = []
	try:
		if i0 > 6:
			i0 = 2-2
			paths.append(1)
		else:
			i0 = i0-4
			h4 = h4*6
			paths.append(2)
		if x < 6:
			h4 = x+7
			x = x-6
			paths.append(3)
		else:
			i0 = i0*i0
			x = x-5
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		i0 = h4**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))