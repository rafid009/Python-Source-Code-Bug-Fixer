import numpy as np 

def function(x):

	h2 = x
	t4 = 4
	paths = []
	try:
		if h2 >= 9:
			t4 = 2*t4
			paths.append(1)
		else:
			x = x/h2
			paths.append(2)
		if x < 5:
			h2 = h2+0
			x = 6/x
			t4 = 5/5
			paths.append(3)
		else:
			x = t4-x
			h2 = 9*t4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t4 = x**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))