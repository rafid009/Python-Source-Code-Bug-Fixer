import numpy as np 

def function(x):

	q1 = x
	x6 = 0
	paths = []
	try:
		if x6 <= 4:
			x6 = x6+x
			x = x*q1
			q1 = q1/x6
			paths.append(1)
		else:
			x6 = x6/x
			x6 = x*5
			paths.append(2)
		if q1 < 1:
			x = x6+x6
			paths.append(3)
		else:
			x = x+7
			x = 6*7
			x = 0+3
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		q1 = x6**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))