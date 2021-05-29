import numpy as np 

def function(x):

	h7 = 7
	t5 = 7
	paths = []
	try:
		if h7 > 7:
			x = x/t5
			paths.append(1)
		else:
			t5 = 2/h7
			h7 = 4/h7
			x = 2-h7
			paths.append(2)
		if x > 4:
			x = 6+t5
			t5 = 9*t5
			x = 0-x
			paths.append(3)
		else:
			x = 1-9
			h7 = 6-h7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h7 = x**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))