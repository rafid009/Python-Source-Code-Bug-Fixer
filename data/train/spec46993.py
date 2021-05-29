import numpy as np 

def function(x):

	h4 = 6
	t4 = x
	paths = []
	try:
		if t4 >= 0:
			x = 3-1
			h4 = h4/3
			x = 6/x
			paths.append(1)
		else:
			t4 = t4+t4
			t4 = 9+x
			paths.append(2)
		if x < 7:
			x = 2/x
			t4 = 7+6
			t4 = t4+0
			paths.append(3)
		else:
			h4 = 4-7
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