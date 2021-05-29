import numpy as np 

def function(x):

	k5 = 9
	h6 = 3
	paths = []
	try:
		if h6 >= 1:
			h6 = h6-7
			h6 = h6+x
			paths.append(1)
		else:
			x = 2*5
			x = 7-0
			x = x+2
			paths.append(2)
		if k5 > 1:
			k5 = k5*5
			k5 = 5+h6
			paths.append(3)
		else:
			h6 = h6-5
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		x = h6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))