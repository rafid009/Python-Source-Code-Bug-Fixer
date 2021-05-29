import numpy as np 

def function(x):

	f1 = 1
	h8 = x
	x = 5
	paths = []
	try:
		if f1 > 6:
			h8 = h8+5
			f1 = 5*f1
			h8 = f1+h8
			paths.append(1)
		else:
			h8 = 1-x
			f1 = 8/f1
			x = 8*x
			paths.append(2)
		if h8 < 6:
			x = 3-f1
			paths.append(3)
		else:
			f1 = f1-8
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		x = h8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))