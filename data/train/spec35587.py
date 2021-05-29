import numpy as np 

def function(x):

	q6 = 8
	t7 = x
	paths = []
	try:
		if q6 <= 0:
			q6 = 1-q6
			q6 = 4+8
			t7 = 6+t7
			paths.append(1)
		else:
			x = x/t7
			x = 1-5
			paths.append(2)
		if x > 5:
			x = 2*4
			paths.append(3)
		else:
			q6 = 9*q6
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