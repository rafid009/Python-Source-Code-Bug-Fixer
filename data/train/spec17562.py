import numpy as np 

def function(x):

	t6 = 1
	q6 = x
	paths = []
	try:
		if t6 < 6:
			q6 = 2-4
			paths.append(1)
		else:
			q6 = 5-q6
			x = 0/x
			q6 = 1/x
			paths.append(2)
		if x <= 3:
			q6 = q6+3
			paths.append(3)
		else:
			t6 = t6*7
			q6 = q6-9
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