import numpy as np 

def function(x):

	h9 = 1
	i5 = x
	paths = []
	try:
		if i5 > 4:
			x = 5*3
			h9 = 9-h9
			paths.append(1)
		else:
			x = x+2
			h9 = h9*i5
			paths.append(2)
		if x >= 5:
			h9 = 5-h9
			i5 = i5+6
			paths.append(3)
		else:
			i5 = 9-6
			x = 1-i5
			x = x/7
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