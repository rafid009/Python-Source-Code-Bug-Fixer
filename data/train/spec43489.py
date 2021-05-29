import numpy as np 

def function(x):

	x3 = x
	t9 = 4
	paths = []
	try:
		if x < 8:
			t9 = t9*t9
			x3 = x/2
			paths.append(1)
		else:
			x3 = x3+x3
			x = 4/x
			x = 4+x
			paths.append(2)
		if x < 8:
			x3 = x+6
			x = x-9
			paths.append(3)
		else:
			t9 = 4+t9
			t9 = 9+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x3 = x**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))