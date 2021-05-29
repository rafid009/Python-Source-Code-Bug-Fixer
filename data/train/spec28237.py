import numpy as np 

def function(x):

	y7 = 8
	q2 = 9
	paths = []
	try:
		if q2 >= 6:
			q2 = y7+q2
			paths.append(1)
		else:
			q2 = x/q2
			paths.append(2)
		if y7 > 2:
			q2 = q2+x
			y7 = y7/3
			paths.append(3)
		else:
			q2 = 2-q2
			y7 = y7+8
			y7 = q2+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q2 = x**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))