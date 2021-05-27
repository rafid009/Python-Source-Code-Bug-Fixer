import numpy as np 

def function(x):

	r4 = x
	h6 = x
	paths = []
	try:
		if h6 > 5:
			r4 = 2*h6
			x = 5*h6
			paths.append(1)
		else:
			h6 = 1/h6
			x = h6/4
			h6 = 3-h6
			paths.append(2)
		if r4 >= 9:
			x = x*0
			paths.append(3)
		else:
			r4 = 5-r4
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