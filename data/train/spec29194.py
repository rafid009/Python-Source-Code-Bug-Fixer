import numpy as np 

def function(x):

	q6 = 2
	e6 = 5
	paths = []
	try:
		if x < 6:
			x = x*1
			x = x/7
			paths.append(1)
		else:
			e6 = e6-1
			e6 = 9/3
			paths.append(2)
		if x > 9:
			q6 = 4/q6
			paths.append(3)
		else:
			q6 = 7*3
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