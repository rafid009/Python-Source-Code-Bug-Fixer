import numpy as np 

def function(x):

	i2 = 4
	h4 = x
	paths = []
	try:
		if h4 < 5:
			x = 2*h4
			paths.append(1)
		else:
			i2 = 1-1
			h4 = 9-h4
			h4 = 6+h4
			paths.append(2)
		if i2 > 1:
			i2 = 5*i2
			x = i2*i2
			x = x/i2
			paths.append(3)
		else:
			x = x-h4
			h4 = h4-h4
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		h4 = h4**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))