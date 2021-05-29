import numpy as np 

def function(x):

	t3 = 3
	h8 = 3
	paths = []
	try:
		if t3 >= 6:
			h8 = 3*5
			x = h8*t3
			x = 7-1
			paths.append(1)
		else:
			h8 = h8-9
			h8 = h8*1
			x = x+7
			paths.append(2)
		if t3 > 8:
			x = t3-4
			x = 5-h8
			t3 = 2*7
			paths.append(3)
		else:
			x = x*t3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))