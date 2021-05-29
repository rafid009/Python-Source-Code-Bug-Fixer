import numpy as np 

def function(x):

	t0 = x
	h6 = 6
	paths = []
	try:
		if x < 3:
			h6 = h6-5
			h6 = t0+h6
			h6 = x+h6
			paths.append(1)
		else:
			t0 = 5*2
			h6 = t0-h6
			x = x-2
			paths.append(2)
		if h6 >= 6:
			x = 5/x
			h6 = h6/h6
			paths.append(3)
		else:
			t0 = x/4
			t0 = 9*0
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