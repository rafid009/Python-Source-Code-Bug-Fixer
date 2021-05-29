import numpy as np 

def function(x):

	q7 = 4
	d7 = x
	paths = []
	try:
		if q7 >= 4:
			x = 8+x
			q7 = 5+q7
			q7 = d7/3
			paths.append(1)
		else:
			x = 5*d7
			paths.append(2)
		if q7 > 1:
			x = 5+9
			x = x-9
			paths.append(3)
		else:
			x = x*8
			d7 = d7+d7
			d7 = d7-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d7 = x**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))