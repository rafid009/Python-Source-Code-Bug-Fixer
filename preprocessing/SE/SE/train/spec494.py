import numpy as np 

def function(x):

	h3 = x
	t0 = 7
	paths = []
	try:
		if x > 1:
			h3 = h3-9
			h3 = 0*h3
			x = 3-x
			paths.append(1)
		else:
			t0 = h3+4
			t0 = t0*2
			paths.append(2)
		if h3 < 5:
			x = 2*x
			t0 = 1/t0
			paths.append(3)
		else:
			x = 3/8
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		t0 = h3**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))