import numpy as np 

def function(x):

	q7 = 9
	d1 = x
	x = 7
	paths = []
	try:
		if d1 <= 9:
			x = 8*6
			x = x*q7
			paths.append(1)
		else:
			q7 = d1-d1
			x = 3*7
			paths.append(2)
		if q7 >= 3:
			q7 = x/x
			paths.append(3)
		else:
			q7 = d1*q7
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		d1 = d1**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))