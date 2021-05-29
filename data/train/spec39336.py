import numpy as np 

def function(x):

	q1 = x
	d6 = x
	x = x
	paths = []
	try:
		if q1 >= 1:
			x = d6*x
			d6 = d6/x
			paths.append(1)
		else:
			q1 = q1+0
			x = x-d6
			paths.append(2)
		if x > 2:
			q1 = d6-4
			q1 = q1/2
			paths.append(3)
		else:
			q1 = 8+1
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		x = d6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))