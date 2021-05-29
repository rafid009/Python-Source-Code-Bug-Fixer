import numpy as np 

def function(x):

	q2 = 5
	d7 = 9
	paths = []
	try:
		if q2 < 0:
			x = q2-x
			d7 = 3*d7
			paths.append(1)
		else:
			d7 = d7-d7
			paths.append(2)
		if q2 > 1:
			d7 = 6/5
			q2 = q2+6
			d7 = x+0
			paths.append(3)
		else:
			x = x+q2
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		q2 = d7**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))