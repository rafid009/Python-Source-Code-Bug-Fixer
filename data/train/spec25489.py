import numpy as np 

def function(x):

	t5 = x
	x5 = 3
	paths = []
	try:
		if x >= 4:
			x = 8/x
			paths.append(1)
		else:
			t5 = t5/2
			x5 = 5*t5
			t5 = 3/t5
			paths.append(2)
		if x >= 1:
			x5 = x5-7
			x5 = x5-4
			paths.append(3)
		else:
			t5 = 2/2
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