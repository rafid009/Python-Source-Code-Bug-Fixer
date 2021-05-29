import numpy as np 

def function(x):

	a6 = 6
	h6 = 4
	paths = []
	try:
		if x > 5:
			h6 = 3*h6
			x = x+7
			h6 = 4/h6
			paths.append(1)
		else:
			a6 = 0+1
			h6 = 2*5
			h6 = 6/a6
			paths.append(2)
		if x <= 3:
			x = x+x
			paths.append(3)
		else:
			h6 = h6-a6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a6 = x**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))