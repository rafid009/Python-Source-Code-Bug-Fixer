import numpy as np 

def function(x):

	j8 = x
	h8 = 4
	x = 8
	paths = []
	try:
		if h8 > 4:
			x = x+5
			x = x/2
			j8 = j8-6
			paths.append(1)
		else:
			x = j8+x
			h8 = 4*h8
			paths.append(2)
		if j8 > 3:
			x = x-h8
			j8 = j8/7
			h8 = h8*1
			paths.append(3)
		else:
			h8 = h8-6
			x = x+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))