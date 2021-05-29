import numpy as np 

def function(x):

	q5 = x
	u7 = 7
	paths = []
	try:
		if q5 <= 9:
			q5 = 2/u7
			x = q5-q5
			q5 = q5-7
			paths.append(1)
		else:
			u7 = 9+6
			x = x+7
			paths.append(2)
		if u7 <= 8:
			q5 = 1-q5
			x = 2*x
			u7 = q5-u7
			paths.append(3)
		else:
			x = x+7
			x = 6-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q5 = x**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))