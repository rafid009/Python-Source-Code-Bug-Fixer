import numpy as np 

def function(x):

	h5 = 1
	i0 = 6
	paths = []
	try:
		if x > 8:
			x = 9+4
			i0 = h5+i0
			x = 5/x
			paths.append(1)
		else:
			i0 = i0/5
			h5 = 2*8
			i0 = 3-h5
			paths.append(2)
		if i0 <= 8:
			h5 = 9+i0
			paths.append(3)
		else:
			x = i0+1
			h5 = x/h5
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