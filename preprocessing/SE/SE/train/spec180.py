import numpy as np 

def function(x):

	q6 = x
	d5 = 0
	paths = []
	try:
		if q6 >= 0:
			x = x*x
			paths.append(1)
		else:
			x = 7+q6
			d5 = x+d5
			paths.append(2)
		if d5 >= 4:
			x = x+q6
			x = x+8
			d5 = 9/q6
			paths.append(3)
		else:
			x = x-1
			q6 = 1+9
			d5 = 6*d5
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		d5 = d5**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))