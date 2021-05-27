import numpy as np 

def function(x):

	q6 = 3
	d9 = x
	paths = []
	try:
		if d9 <= 0:
			d9 = q6*d9
			q6 = q6+2
			q6 = q6*d9
			paths.append(1)
		else:
			x = x*8
			q6 = 7/x
			paths.append(2)
		if q6 <= 9:
			d9 = 4/d9
			d9 = d9/4
			q6 = 3/x
			paths.append(3)
		else:
			d9 = d9-x
			x = x/2
			d9 = d9+2
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		q6 = d9**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))