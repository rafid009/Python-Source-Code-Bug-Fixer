import numpy as np 

def function(x):

	q6 = x
	d6 = 3
	paths = []
	try:
		if q6 > 8:
			d6 = 3-d6
			paths.append(1)
		else:
			d6 = d6+9
			q6 = q6/q6
			q6 = x-1
			paths.append(2)
		if d6 < 6:
			x = 2-d6
			d6 = 9*2
			x = x/7
			paths.append(3)
		else:
			q6 = x*q6
			x = 7-x
			q6 = d6/d6
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