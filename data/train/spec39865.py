import numpy as np 

def function(x):

	d1 = 9
	q7 = x
	x = 3
	paths = []
	try:
		if x >= 9:
			x = x/d1
			paths.append(1)
		else:
			x = 3/x
			x = q7*d1
			paths.append(2)
		if d1 > 7:
			x = x+5
			paths.append(3)
		else:
			x = x*6
			d1 = 7+d1
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