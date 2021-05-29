import numpy as np 

def function(x):

	x1 = 2
	h2 = x
	paths = []
	try:
		if h2 >= 3:
			x = x+9
			paths.append(1)
		else:
			x = x1-5
			x = 5*x
			x = 4-x
			paths.append(2)
		if x < 4:
			x1 = x1-8
			x = x-3
			x = 3-x
			paths.append(3)
		else:
			x1 = x1+h2
			x = 0+9
			h2 = 1*7
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		x1 = x1**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))