import numpy as np 

def function(x):

	q7 = x
	v9 = x
	paths = []
	try:
		if q7 <= 9:
			v9 = v9-5
			x = q7*9
			paths.append(1)
		else:
			x = 5/q7
			v9 = 6+q7
			paths.append(2)
		if q7 > 5:
			v9 = 8-9
			x = 0/x
			v9 = v9*3
			paths.append(3)
		else:
			q7 = q7+1
			q7 = q7*q7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))