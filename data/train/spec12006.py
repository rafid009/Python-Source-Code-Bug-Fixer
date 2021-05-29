import numpy as np 

def function(x):

	h5 = 2
	e8 = 4
	paths = []
	try:
		if e8 >= 5:
			x = e8+x
			e8 = 3-1
			paths.append(1)
		else:
			h5 = 6-e8
			paths.append(2)
		if e8 < 8:
			e8 = e8*3
			h5 = x*0
			e8 = 3+e8
			paths.append(3)
		else:
			x = 2/x
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