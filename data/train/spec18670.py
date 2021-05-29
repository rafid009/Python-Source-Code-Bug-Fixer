import numpy as np 

def function(x):

	q7 = x
	d8 = x
	x = 1
	paths = []
	try:
		if q7 >= 8:
			x = 8-x
			q7 = q7-1
			paths.append(1)
		else:
			x = x*5
			d8 = 0+x
			paths.append(2)
		if d8 <= 8:
			d8 = d8/d8
			d8 = 5*6
			d8 = 9+1
			paths.append(3)
		else:
			q7 = 8*q7
			d8 = d8/d8
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		q7 = q7**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))