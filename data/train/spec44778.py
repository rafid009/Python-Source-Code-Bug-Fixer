import numpy as np 

def function(x):

	t6 = 1
	b6 = 0
	paths = []
	try:
		if x >= 9:
			t6 = 6-t6
			x = x/x
			paths.append(1)
		else:
			x = b6+1
			x = x-9
			paths.append(2)
		if x > 2:
			x = 8*x
			paths.append(3)
		else:
			b6 = b6*b6
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