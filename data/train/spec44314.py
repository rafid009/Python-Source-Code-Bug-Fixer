import numpy as np 

def function(x):

	i2 = 6
	h8 = 5
	paths = []
	try:
		if x <= 4:
			i2 = i2+3
			paths.append(1)
		else:
			i2 = i2*i2
			h8 = i2/h8
			paths.append(2)
		if h8 < 6:
			h8 = 6*h8
			paths.append(3)
		else:
			x = 1-x
			i2 = i2+2
			h8 = 5+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i2 = x**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))