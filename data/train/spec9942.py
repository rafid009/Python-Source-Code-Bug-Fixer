import numpy as np 

def function(x):

	x3 = x
	t9 = 4
	paths = []
	try:
		if x > 6:
			x3 = t9-x3
			x3 = x3-3
			x = x3+x
			paths.append(1)
		else:
			x = x*7
			x3 = x/x3
			x3 = 2+x3
			paths.append(2)
		if x3 < 7:
			x = 4-t9
			t9 = 6-t9
			paths.append(3)
		else:
			t9 = x+t9
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x = x3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))