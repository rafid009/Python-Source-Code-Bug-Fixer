import numpy as np 

def function(x):

	t7 = 9
	h5 = x
	paths = []
	try:
		if x > 6:
			t7 = x/t7
			x = x+9
			t7 = t7/h5
			paths.append(1)
		else:
			t7 = 0/8
			h5 = h5/6
			paths.append(2)
		if t7 < 5:
			h5 = x/h5
			h5 = x+h5
			paths.append(3)
		else:
			h5 = 5-h5
			h5 = h5+1
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