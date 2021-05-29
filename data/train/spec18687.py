import numpy as np 

def function(x):

	q9 = 6
	t3 = x
	paths = []
	try:
		if x < 7:
			q9 = 5*t3
			paths.append(1)
		else:
			x = 3*x
			q9 = q9-2
			paths.append(2)
		if q9 < 2:
			x = 5/x
			x = 8-x
			paths.append(3)
		else:
			q9 = q9/1
			q9 = 3-t3
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		q9 = q9**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))