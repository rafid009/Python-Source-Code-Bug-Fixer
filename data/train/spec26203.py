import numpy as np 

def function(x):

	x6 = 1
	q9 = 3
	x = x
	paths = []
	try:
		if q9 > 8:
			x = q9+7
			x6 = x6*3
			x6 = 5/x6
			paths.append(1)
		else:
			q9 = 2/q9
			q9 = x+7
			paths.append(2)
		if x >= 5:
			x = x6*6
			q9 = 1*x
			paths.append(3)
		else:
			q9 = 3*4
			x = x*2
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