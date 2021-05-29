import numpy as np 

def function(x):

	q7 = x
	d0 = x
	paths = []
	try:
		if d0 < 4:
			x = x*7
			d0 = d0+1
			d0 = d0-x
			paths.append(1)
		else:
			d0 = d0/5
			q7 = x/q7
			paths.append(2)
		if q7 < 3:
			d0 = d0-7
			q7 = 3-q7
			q7 = q7/x
			paths.append(3)
		else:
			x = 5+x
			d0 = x/d0
			q7 = 1*7
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		x = q7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))