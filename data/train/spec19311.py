import numpy as np 

def function(x):

	t3 = x
	q1 = x
	paths = []
	try:
		if x > 6:
			t3 = t3-t3
			q1 = 5-2
			x = x/x
			paths.append(1)
		else:
			x = 6*9
			paths.append(2)
		if x >= 0:
			q1 = 9-5
			x = x-2
			paths.append(3)
		else:
			q1 = q1*1
			t3 = 1-t3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q1 = x**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))