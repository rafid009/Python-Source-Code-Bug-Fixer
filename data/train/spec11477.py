import numpy as np 

def function(x):

	q6 = x
	d8 = 2
	paths = []
	try:
		if d8 < 8:
			x = 1+q6
			x = q6/x
			d8 = 8-d8
			paths.append(1)
		else:
			x = x+1
			paths.append(2)
		if q6 < 3:
			q6 = 3/1
			paths.append(3)
		else:
			x = x/4
			x = x/x
			d8 = 1-2
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		q6 = d8**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))