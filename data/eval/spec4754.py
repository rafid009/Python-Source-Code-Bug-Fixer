import numpy as np 

def function(x):

	i7 = 1
	q1 = 3
	paths = []
	try:
		if q1 < 5:
			i7 = x/i7
			i7 = i7*x
			paths.append(1)
		else:
			i7 = i7+x
			paths.append(2)
		if x < 8:
			q1 = 9/q1
			paths.append(3)
		else:
			q1 = q1*6
			q1 = q1*7
			x = 3+6
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