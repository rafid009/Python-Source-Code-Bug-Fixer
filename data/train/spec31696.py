import numpy as np 

def function(x):

	d5 = x
	q7 = 5
	paths = []
	try:
		if q7 > 0:
			q7 = 1-q7
			paths.append(1)
		else:
			q7 = q7/4
			d5 = d5-q7
			x = x/9
			paths.append(2)
		if d5 >= 1:
			d5 = 2-2
			d5 = d5+d5
			x = d5*5
			paths.append(3)
		else:
			q7 = 4*q7
			x = 4/d5
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		d5 = q7**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))