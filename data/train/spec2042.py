import numpy as np 

def function(x):

	v4 = 1
	q7 = 4
	paths = []
	try:
		if x >= 8:
			q7 = x*q7
			paths.append(1)
		else:
			v4 = q7/q7
			q7 = q7*1
			x = x+3
			paths.append(2)
		if v4 > 7:
			v4 = v4+q7
			q7 = v4-q7
			x = x-7
			paths.append(3)
		else:
			q7 = 7/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v4 = x**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))