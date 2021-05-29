import numpy as np 

def function(x):

	u5 = x
	h9 = 0
	paths = []
	try:
		if h9 >= 0:
			u5 = 3+u5
			paths.append(1)
		else:
			h9 = x+0
			x = x/3
			paths.append(2)
		if h9 < 5:
			h9 = 4+h9
			x = x-5
			h9 = u5*x
			paths.append(3)
		else:
			h9 = h9*4
			h9 = h9-0
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		u5 = u5**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))