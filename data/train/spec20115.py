import numpy as np 

def function(x):

	t9 = 3
	q8 = 2
	paths = []
	try:
		if x >= 5:
			x = 1/q8
			paths.append(1)
		else:
			x = q8*3
			t9 = t9/2
			paths.append(2)
		if q8 >= 7:
			x = t9-x
			paths.append(3)
		else:
			q8 = q8-6
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		x = q8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))