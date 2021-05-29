import numpy as np 

def function(x):

	q7 = 0
	d1 = x
	paths = []
	try:
		if q7 < 0:
			q7 = q7/x
			d1 = d1+6
			paths.append(1)
		else:
			x = d1+x
			x = x-x
			paths.append(2)
		if q7 <= 8:
			q7 = d1+1
			q7 = q7/6
			q7 = q7/9
			paths.append(3)
		else:
			d1 = 0/1
			q7 = q7*x
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		d1 = q7**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))