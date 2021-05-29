import numpy as np 

def function(x):

	q2 = 5
	y5 = 2
	paths = []
	try:
		if x > 7:
			q2 = q2/4
			x = 1*x
			paths.append(1)
		else:
			q2 = y5/4
			paths.append(2)
		if q2 <= 3:
			q2 = x-q2
			y5 = y5+1
			x = x/1
			paths.append(3)
		else:
			q2 = 7/q2
			x = 2*3
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