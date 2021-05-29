import numpy as np 

def function(x):

	i2 = x
	h7 = 7
	paths = []
	try:
		if i2 > 8:
			x = 9*x
			paths.append(1)
		else:
			h7 = h7-8
			paths.append(2)
		if x <= 5:
			h7 = 5/h7
			paths.append(3)
		else:
			i2 = h7+1
			i2 = i2/3
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