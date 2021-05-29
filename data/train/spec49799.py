import numpy as np 

def function(x):

	q9 = x
	q0 = 0
	paths = []
	try:
		if x < 7:
			q0 = q0-x
			paths.append(1)
		else:
			x = 6/9
			q9 = 8+9
			paths.append(2)
		if q9 <= 1:
			q0 = q0/q9
			paths.append(3)
		else:
			q0 = 1-q0
			x = 2/1
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		q9 = q0**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))