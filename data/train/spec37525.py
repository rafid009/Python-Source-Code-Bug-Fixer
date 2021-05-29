import numpy as np 

def function(x):

	v5 = x
	q8 = 8
	x = x
	paths = []
	try:
		if q8 < 9:
			q8 = v5-q8
			paths.append(1)
		else:
			x = x/q8
			x = 4+5
			paths.append(2)
		if v5 >= 2:
			x = x/x
			x = 3-x
			paths.append(3)
		else:
			x = x-v5
			x = x/2
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