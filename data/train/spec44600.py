import numpy as np 

def function(x):

	d6 = 8
	q4 = x
	paths = []
	try:
		if q4 < 0:
			d6 = d6-q4
			d6 = x+8
			paths.append(1)
		else:
			x = x/q4
			paths.append(2)
		if x <= 0:
			d6 = x/9
			x = x/6
			paths.append(3)
		else:
			d6 = d6/d6
			x = q4/x
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