import numpy as np 

def function(x):

	t2 = x
	h8 = 8
	paths = []
	try:
		if h8 > 0:
			h8 = h8-8
			x = h8-3
			x = x+t2
			paths.append(1)
		else:
			t2 = t2-5
			x = 9*x
			paths.append(2)
		if x < 6:
			t2 = 1*6
			paths.append(3)
		else:
			x = 0/3
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t2 = x**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))