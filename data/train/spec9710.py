import numpy as np 

def function(x):

	t9 = x
	v0 = x
	x = 3
	paths = []
	try:
		if v0 < 0:
			x = 9-t9
			paths.append(1)
		else:
			t9 = 3*t9
			paths.append(2)
		if v0 > 2:
			t9 = t9*t9
			paths.append(3)
		else:
			x = 8+x
			x = x/8
			t9 = t9-8
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