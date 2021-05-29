import numpy as np 

def function(x):

	h3 = x
	f5 = x
	paths = []
	try:
		if f5 < 4:
			h3 = f5*f5
			h3 = 4*h3
			x = x+h3
			paths.append(1)
		else:
			x = 6/x
			x = 6/f5
			paths.append(2)
		if h3 > 5:
			h3 = h3*6
			x = x*7
			paths.append(3)
		else:
			h3 = 3/x
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