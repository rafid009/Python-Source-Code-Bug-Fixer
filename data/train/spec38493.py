import numpy as np 

def function(x):

	h5 = 8
	j1 = x
	paths = []
	try:
		if j1 < 0:
			j1 = j1*x
			paths.append(1)
		else:
			h5 = h5+5
			h5 = h5+h5
			j1 = j1-3
			paths.append(2)
		if x > 6:
			x = x+4
			j1 = x*j1
			x = j1/3
			paths.append(3)
		else:
			x = 0+6
			x = 8/x
			x = j1+7
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		h5 = j1**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))