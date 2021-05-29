import numpy as np 

def function(x):

	t8 = x
	h6 = 5
	paths = []
	try:
		if h6 >= 8:
			h6 = h6/7
			h6 = 9+h6
			h6 = h6-h6
			paths.append(1)
		else:
			x = t8+t8
			h6 = h6*h6
			h6 = 6/x
			paths.append(2)
		if t8 <= 3:
			t8 = t8-5
			h6 = h6+t8
			paths.append(3)
		else:
			h6 = h6+h6
			x = x*2
			h6 = 7/h6
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		h6 = h6**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))