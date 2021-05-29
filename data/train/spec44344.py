import numpy as np 

def function(x):

	j0 = x
	h5 = x
	paths = []
	try:
		if j0 > 2:
			x = x-9
			x = x-j0
			paths.append(1)
		else:
			h5 = 9+h5
			paths.append(2)
		if x <= 8:
			x = x*2
			x = 9*6
			paths.append(3)
		else:
			x = h5/5
			j0 = j0+7
			x = 1+x
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