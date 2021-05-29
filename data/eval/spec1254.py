import numpy as np 

def function(x):

	r8 = 6
	h6 = x
	paths = []
	try:
		if x >= 3:
			r8 = 7/r8
			r8 = x/r8
			h6 = 9*x
			paths.append(1)
		else:
			x = 4+8
			h6 = h6+9
			x = h6/4
			paths.append(2)
		if h6 < 4:
			r8 = h6/7
			paths.append(3)
		else:
			x = 0-r8
			r8 = 1+h6
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		r8 = h6**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))