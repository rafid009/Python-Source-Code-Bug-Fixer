import numpy as np 

def function(x):

	v8 = x
	q7 = 4
	paths = []
	try:
		if q7 > 2:
			q7 = 1+2
			paths.append(1)
		else:
			q7 = x-q7
			paths.append(2)
		if v8 < 1:
			x = 6-7
			x = x*2
			paths.append(3)
		else:
			x = x-v8
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