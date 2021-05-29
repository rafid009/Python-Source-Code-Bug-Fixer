import numpy as np 

def function(x):

	x7 = x
	t2 = 2
	paths = []
	try:
		if x < 5:
			t2 = t2/t2
			t2 = x7*t2
			paths.append(1)
		else:
			x = 5+x
			x7 = x7/7
			x = x*x
			paths.append(2)
		if x7 < 8:
			x = 0-x
			paths.append(3)
		else:
			x = x*x7
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