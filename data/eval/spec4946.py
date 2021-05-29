import numpy as np 

def function(x):

	h0 = 4
	j1 = x
	paths = []
	try:
		if x >= 3:
			j1 = j1+2
			h0 = x-2
			paths.append(1)
		else:
			j1 = j1*3
			paths.append(2)
		if x > 7:
			j1 = j1+6
			paths.append(3)
		else:
			h0 = h0*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j1 = x**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))