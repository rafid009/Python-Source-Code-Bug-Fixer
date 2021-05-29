import numpy as np 

def function(x):

	q7 = x
	o6 = 7
	paths = []
	try:
		if q7 < 8:
			x = o6+x
			paths.append(1)
		else:
			x = 4*x
			q7 = q7+1
			o6 = q7/6
			paths.append(2)
		if o6 < 5:
			x = x+o6
			x = 7/x
			paths.append(3)
		else:
			o6 = 7/1
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