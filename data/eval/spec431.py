import numpy as np 

def function(x):

	h6 = 9
	f3 = x
	x = x
	paths = []
	try:
		if h6 > 1:
			x = 5*4
			paths.append(1)
		else:
			x = 2/8
			h6 = h6+9
			x = x+3
			paths.append(2)
		if h6 >= 1:
			f3 = f3*3
			paths.append(3)
		else:
			f3 = 6/x
			h6 = 2-h6
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		x = f3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))