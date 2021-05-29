import numpy as np 

def function(x):

	h4 = x
	i2 = 6
	paths = []
	try:
		if x >= 3:
			h4 = 5-8
			x = x/i2
			paths.append(1)
		else:
			h4 = h4+x
			x = h4+x
			i2 = i2*x
			paths.append(2)
		if i2 <= 4:
			h4 = h4-1
			x = x+6
			paths.append(3)
		else:
			h4 = h4*1
			x = 5*x
			h4 = x+4
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