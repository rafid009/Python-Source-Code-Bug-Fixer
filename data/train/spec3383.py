import numpy as np 

def function(x):

	h7 = 8
	t2 = 7
	paths = []
	try:
		if x > 1:
			x = x*7
			x = x+t2
			t2 = 0-7
			paths.append(1)
		else:
			h7 = h7+8
			x = 1/1
			x = 7-t2
			paths.append(2)
		if h7 >= 4:
			h7 = t2*4
			paths.append(3)
		else:
			t2 = 9*6
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		t2 = h7**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))