import numpy as np 

def function(x):

	q8 = 6
	e2 = 3
	paths = []
	try:
		if x > 7:
			x = 1-e2
			e2 = e2*x
			x = x/q8
			paths.append(1)
		else:
			x = x*4
			paths.append(2)
		if x < 9:
			q8 = q8/q8
			q8 = q8*6
			q8 = x+4
			paths.append(3)
		else:
			x = x+4
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