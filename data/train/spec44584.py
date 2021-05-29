import numpy as np 

def function(x):

	t0 = x
	q3 = x
	paths = []
	try:
		if q3 >= 7:
			x = 3+x
			x = 6-x
			paths.append(1)
		else:
			x = 5/x
			q3 = q3*t0
			paths.append(2)
		if q3 <= 9:
			x = q3/x
			paths.append(3)
		else:
			q3 = q3+7
			q3 = q3+8
			q3 = 4+q3
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		q3 = t0**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))