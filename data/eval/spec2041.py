import numpy as np 

def function(x):

	h2 = x
	t1 = 3
	x = 4
	paths = []
	try:
		if t1 >= 5:
			h2 = h2*4
			h2 = h2-t1
			h2 = x-h2
			paths.append(1)
		else:
			t1 = 3*6
			t1 = t1+3
			paths.append(2)
		if h2 > 3:
			t1 = t1-7
			h2 = h2/8
			paths.append(3)
		else:
			t1 = 4+t1
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		t1 = h2**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))