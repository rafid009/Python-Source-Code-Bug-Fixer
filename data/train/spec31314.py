import numpy as np 

def function(x):

	f5 = x
	h9 = x
	x = 3
	paths = []
	try:
		if f5 >= 7:
			h9 = h9*x
			paths.append(1)
		else:
			x = h9*2
			paths.append(2)
		if h9 < 5:
			h9 = h9*9
			h9 = h9-5
			paths.append(3)
		else:
			x = 0*x
			f5 = f5+2
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		x = f5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))