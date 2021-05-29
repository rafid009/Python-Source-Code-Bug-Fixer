import numpy as np 

def function(x):

	q7 = x
	j9 = x
	paths = []
	try:
		if q7 > 4:
			j9 = 2-j9
			x = x/x
			paths.append(1)
		else:
			j9 = q7*6
			j9 = 8-1
			j9 = j9-8
			paths.append(2)
		if q7 < 8:
			x = x*2
			q7 = 4-q7
			x = 6-8
			paths.append(3)
		else:
			x = x*6
			q7 = q7/j9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q7 = x**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))