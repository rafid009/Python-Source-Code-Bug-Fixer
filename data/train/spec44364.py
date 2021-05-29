import numpy as np 

def function(x):

	k4 = 6
	h9 = 1
	paths = []
	try:
		if k4 > 6:
			k4 = 0+6
			paths.append(1)
		else:
			x = x*x
			h9 = 6*h9
			x = 4*x
			paths.append(2)
		if k4 >= 5:
			k4 = 4-k4
			k4 = 0+k4
			paths.append(3)
		else:
			k4 = k4+h9
			x = x*2
			k4 = 1*k4
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		x = k4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))