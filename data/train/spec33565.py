import numpy as np 

def function(x):

	j1 = 5
	h5 = x
	paths = []
	try:
		if x >= 4:
			h5 = 8*h5
			paths.append(1)
		else:
			h5 = 8/x
			h5 = h5*3
			paths.append(2)
		if x > 3:
			j1 = j1-j1
			h5 = 6/9
			j1 = j1+9
			paths.append(3)
		else:
			x = x+x
			h5 = 5-h5
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		x = h5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))