import numpy as np 

def function(x):

	q4 = 4
	x0 = 6
	paths = []
	try:
		if x0 < 5:
			q4 = q4+8
			x0 = 5-4
			paths.append(1)
		else:
			x0 = x0/4
			q4 = q4+1
			q4 = 3-q4
			paths.append(2)
		if x0 > 6:
			x = q4+x
			paths.append(3)
		else:
			x0 = x/4
			q4 = q4-9
			x = x+7
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