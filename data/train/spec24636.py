import numpy as np 

def function(x):

	q9 = 4
	d8 = 4
	paths = []
	try:
		if q9 < 2:
			x = 2+8
			d8 = d8*1
			paths.append(1)
		else:
			q9 = q9+d8
			paths.append(2)
		if d8 >= 8:
			q9 = q9/d8
			x = x*6
			paths.append(3)
		else:
			q9 = q9-0
			q9 = x/q9
			x = x*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q9 = x**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))