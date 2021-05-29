import numpy as np 

def function(x):

	v8 = x
	q7 = 3
	paths = []
	try:
		if q7 < 8:
			v8 = v8/1
			x = x/8
			paths.append(1)
		else:
			x = 7*x
			v8 = x/3
			paths.append(2)
		if v8 < 3:
			q7 = q7*8
			q7 = q7+0
			paths.append(3)
		else:
			x = 0*q7
			q7 = q7-4
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