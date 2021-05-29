import numpy as np 

def function(x):

	g5 = 3
	q6 = 9
	paths = []
	try:
		if q6 > 3:
			g5 = 3/g5
			q6 = 4/q6
			q6 = q6-6
			paths.append(1)
		else:
			q6 = 1+0
			q6 = q6*x
			x = q6-7
			paths.append(2)
		if g5 < 8:
			x = x-0
			q6 = 5-q6
			paths.append(3)
		else:
			x = 5-2
			x = x/9
			x = 6/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q6 = x**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))