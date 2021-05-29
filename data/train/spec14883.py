import numpy as np 

def function(x):

	a1 = 9
	h9 = 9
	paths = []
	try:
		if h9 >= 7:
			h9 = h9*8
			paths.append(1)
		else:
			h9 = x+3
			x = 2+x
			x = x+7
			paths.append(2)
		if a1 >= 2:
			x = 7-a1
			h9 = a1+h9
			h9 = h9*5
			paths.append(3)
		else:
			a1 = x-a1
			h9 = h9-h9
			a1 = 5/a1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a1 = x**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))