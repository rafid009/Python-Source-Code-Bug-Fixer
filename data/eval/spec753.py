import numpy as np 

def function(x):

	q3 = x
	t0 = 3
	paths = []
	try:
		if x >= 3:
			t0 = t0+2
			paths.append(1)
		else:
			x = x-4
			paths.append(2)
		if x >= 9:
			t0 = t0+t0
			q3 = 8/q3
			x = x*q3
			paths.append(3)
		else:
			x = 0/5
			q3 = 2-q3
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		q3 = q3**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))