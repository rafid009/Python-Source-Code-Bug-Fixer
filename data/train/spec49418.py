import numpy as np 

def function(x):

	q9 = x
	d0 = 3
	paths = []
	try:
		if d0 >= 8:
			x = x+d0
			d0 = q9-9
			paths.append(1)
		else:
			q9 = q9/x
			x = x-1
			q9 = q9-3
			paths.append(2)
		if q9 < 3:
			x = x+d0
			d0 = d0+d0
			paths.append(3)
		else:
			x = 7*9
			q9 = 5+q9
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