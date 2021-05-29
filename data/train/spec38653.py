import numpy as np 

def function(x):

	q4 = 5
	d8 = 9
	paths = []
	try:
		if q4 > 3:
			d8 = 6*d8
			d8 = d8*0
			x = 8+x
			paths.append(1)
		else:
			q4 = q4/1
			x = d8+4
			q4 = q4*x
			paths.append(2)
		if d8 <= 8:
			d8 = d8+x
			d8 = d8+8
			q4 = 4*q4
			paths.append(3)
		else:
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q4 = x**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))