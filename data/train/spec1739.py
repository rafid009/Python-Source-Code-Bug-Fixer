import numpy as np 

def function(x):

	f7 = x
	h4 = x
	paths = []
	try:
		if h4 <= 8:
			h4 = f7+5
			h4 = h4-9
			paths.append(1)
		else:
			f7 = 9+5
			paths.append(2)
		if x > 0:
			h4 = 2-h4
			x = f7*x
			x = x+f7
			paths.append(3)
		else:
			h4 = h4-h4
			x = 6*5
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		x = f7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))