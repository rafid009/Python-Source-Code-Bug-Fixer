import numpy as np 

def function(x):

	t0 = 2
	h1 = x
	paths = []
	try:
		if h1 >= 3:
			t0 = 8-h1
			t0 = t0+t0
			x = 4-x
			paths.append(1)
		else:
			x = x/t0
			t0 = t0-5
			t0 = h1/1
			paths.append(2)
		if t0 <= 2:
			x = x/8
			x = x-1
			h1 = t0/7
			paths.append(3)
		else:
			x = 7/6
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		t0 = t0**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))