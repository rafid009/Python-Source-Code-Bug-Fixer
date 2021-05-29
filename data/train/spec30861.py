import numpy as np 

def function(x):

	n4 = x
	t6 = 4
	paths = []
	try:
		if n4 > 6:
			n4 = n4/n4
			x = 6*t6
			paths.append(1)
		else:
			x = t6-x
			x = 4-6
			t6 = 1*t6
			paths.append(2)
		if t6 > 7:
			n4 = 8/n4
			n4 = x/x
			n4 = n4/n4
			paths.append(3)
		else:
			x = 3-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))