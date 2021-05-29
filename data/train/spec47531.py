import numpy as np 

def function(x):

	q4 = 3
	x5 = x
	paths = []
	try:
		if x5 <= 7:
			q4 = q4-7
			x = 3/3
			x5 = x5/q4
			paths.append(1)
		else:
			q4 = 1+q4
			x = 4/x5
			x = x-2
			paths.append(2)
		if q4 < 1:
			q4 = x5/q4
			paths.append(3)
		else:
			x = x/6
			x5 = x5*q4
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x = x5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))