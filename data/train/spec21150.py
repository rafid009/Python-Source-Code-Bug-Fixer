import numpy as np 

def function(x):

	h8 = 2
	u5 = 6
	paths = []
	try:
		if u5 > 8:
			h8 = h8/9
			x = 6-5
			u5 = 5+h8
			paths.append(1)
		else:
			h8 = h8*u5
			paths.append(2)
		if u5 < 1:
			x = x*5
			x = x-h8
			u5 = u5+9
			paths.append(3)
		else:
			h8 = h8*h8
			x = 6*x
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