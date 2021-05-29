import numpy as np 

def function(x):

	h6 = 0
	a6 = x
	x = x
	paths = []
	try:
		if x < 9:
			h6 = a6+h6
			h6 = x+4
			paths.append(1)
		else:
			a6 = 4-4
			h6 = h6*8
			paths.append(2)
		if h6 > 4:
			a6 = a6-5
			x = a6/x
			x = x+0
			paths.append(3)
		else:
			a6 = a6-7
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		a6 = a6**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))