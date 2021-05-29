import numpy as np 

def function(x):

	h9 = x
	a6 = 1
	paths = []
	try:
		if h9 <= 4:
			x = 9+7
			paths.append(1)
		else:
			a6 = a6-4
			a6 = a6*2
			paths.append(2)
		if x > 4:
			h9 = 2/h9
			paths.append(3)
		else:
			h9 = 1*x
			x = a6+7
			h9 = 0-h9
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		h9 = h9**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))