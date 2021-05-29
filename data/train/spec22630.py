import numpy as np 

def function(x):

	h6 = 0
	t4 = x
	paths = []
	try:
		if t4 > 5:
			x = 0+x
			x = 5/6
			t4 = 0-5
			paths.append(1)
		else:
			x = t4-x
			x = 1/1
			paths.append(2)
		if x > 0:
			h6 = h6/6
			h6 = 4*2
			x = x*t4
			paths.append(3)
		else:
			x = x*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h6 = x**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))