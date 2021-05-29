import numpy as np 

def function(x):

	d8 = x
	q4 = x
	paths = []
	try:
		if q4 <= 7:
			q4 = 9*q4
			q4 = 1+q4
			d8 = 3*d8
			paths.append(1)
		else:
			q4 = q4/6
			paths.append(2)
		if x > 9:
			x = 6/4
			q4 = d8+9
			q4 = q4/1
			paths.append(3)
		else:
			x = x-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d8 = x**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))