import numpy as np 

def function(x):

	q9 = x
	r2 = 9
	paths = []
	try:
		if q9 < 3:
			q9 = 7/q9
			q9 = q9+4
			r2 = 0+r2
			paths.append(1)
		else:
			x = x*3
			x = x+q9
			paths.append(2)
		if x > 2:
			r2 = 3-r2
			paths.append(3)
		else:
			r2 = r2/2
			r2 = 6*7
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