import numpy as np 

def function(x):

	h6 = 5
	k4 = x
	paths = []
	try:
		if x < 4:
			x = 5/1
			h6 = x-h6
			h6 = k4+h6
			paths.append(1)
		else:
			k4 = k4-4
			h6 = k4-h6
			paths.append(2)
		if k4 < 6:
			h6 = 0+h6
			paths.append(3)
		else:
			k4 = k4*k4
			k4 = 6+k4
			h6 = h6-3
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		k4 = h6**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))