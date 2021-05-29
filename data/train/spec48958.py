import numpy as np 

def function(x):

	h3 = 7
	t9 = x
	x = 2
	paths = []
	try:
		if t9 < 3:
			t9 = 2+t9
			paths.append(1)
		else:
			x = x+8
			paths.append(2)
		if x < 8:
			h3 = h3*h3
			t9 = 9-t9
			paths.append(3)
		else:
			t9 = 1-t9
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		x = t9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))