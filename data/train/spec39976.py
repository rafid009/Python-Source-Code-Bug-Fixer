import numpy as np 

def function(x):

	q8 = 4
	t2 = x
	paths = []
	try:
		if t2 >= 8:
			x = 7+x
			paths.append(1)
		else:
			x = 5*t2
			q8 = q8/q8
			x = 8*t2
			paths.append(2)
		if t2 < 9:
			x = 2-x
			paths.append(3)
		else:
			t2 = t2/4
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