import numpy as np 

def function(x):

	h4 = 7
	i2 = 9
	paths = []
	try:
		if h4 > 6:
			h4 = h4/i2
			x = x-2
			paths.append(1)
		else:
			x = 2*x
			h4 = h4-0
			paths.append(2)
		if h4 <= 2:
			i2 = 5-i2
			h4 = h4*7
			paths.append(3)
		else:
			h4 = i2+x
			h4 = x-h4
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		i2 = i2**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))