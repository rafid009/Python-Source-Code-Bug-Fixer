import numpy as np 

def function(x):

	t1 = 1
	h9 = x
	paths = []
	try:
		if h9 <= 0:
			x = 7+7
			paths.append(1)
		else:
			x = 2+8
			paths.append(2)
		if h9 > 2:
			h9 = t1/7
			h9 = 0+9
			x = 6*t1
			paths.append(3)
		else:
			h9 = h9*6
			t1 = t1/x
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		t1 = h9**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))