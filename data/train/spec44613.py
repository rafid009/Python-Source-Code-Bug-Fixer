import numpy as np 

def function(x):

	k4 = 4
	h1 = x
	paths = []
	try:
		if h1 < 9:
			h1 = h1-9
			k4 = 2/3
			k4 = h1-h1
			paths.append(1)
		else:
			h1 = 8*3
			x = k4*x
			paths.append(2)
		if k4 <= 3:
			x = 4*0
			paths.append(3)
		else:
			k4 = k4+6
			h1 = 5+h1
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		h1 = h1**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))