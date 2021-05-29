import numpy as np 

def function(x):

	q9 = x
	j5 = 9
	paths = []
	try:
		if q9 > 9:
			j5 = q9-7
			q9 = q9+x
			j5 = 2-7
			paths.append(1)
		else:
			q9 = 9/q9
			x = x-2
			paths.append(2)
		if j5 >= 3:
			q9 = 3*8
			q9 = j5*q9
			j5 = 8/j5
			paths.append(3)
		else:
			q9 = x*j5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q9 = x**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))