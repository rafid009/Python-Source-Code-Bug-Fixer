import numpy as np 

def function(x):

	t1 = x
	e0 = 3
	paths = []
	try:
		if x > 5:
			t1 = 9-6
			t1 = x-8
			paths.append(1)
		else:
			e0 = x/e0
			paths.append(2)
		if x >= 2:
			t1 = t1-8
			paths.append(3)
		else:
			t1 = 5/4
			e0 = 7+e0
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		x = e0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))