import numpy as np 

def function(x):

	h6 = 8
	t5 = x
	paths = []
	try:
		if h6 >= 6:
			h6 = h6*7
			x = x-4
			paths.append(1)
		else:
			x = 0-x
			x = x/6
			h6 = h6+9
			paths.append(2)
		if x < 9:
			h6 = t5-2
			t5 = t5/9
			paths.append(3)
		else:
			x = x/x
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