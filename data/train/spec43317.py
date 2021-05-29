import numpy as np 

def function(x):

	d3 = 7
	q1 = x
	paths = []
	try:
		if x < 2:
			d3 = 4/1
			x = x/7
			paths.append(1)
		else:
			d3 = 0*0
			x = 6*3
			x = 8*q1
			paths.append(2)
		if q1 < 5:
			d3 = q1*5
			d3 = 2+4
			paths.append(3)
		else:
			d3 = q1/q1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q1 = x**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))