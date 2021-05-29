import numpy as np 

def function(x):

	h5 = 8
	t5 = x
	paths = []
	try:
		if x <= 2:
			h5 = 6-h5
			h5 = h5/5
			paths.append(1)
		else:
			h5 = h5*3
			x = x/8
			t5 = t5+9
			paths.append(2)
		if h5 > 4:
			x = 7/9
			paths.append(3)
		else:
			t5 = t5+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t5 = x**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))