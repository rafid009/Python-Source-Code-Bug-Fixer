import numpy as np 

def function(x):

	q4 = 2
	d6 = x
	paths = []
	try:
		if d6 <= 7:
			d6 = 5-2
			q4 = q4/2
			d6 = x/2
			paths.append(1)
		else:
			d6 = d6*d6
			paths.append(2)
		if d6 <= 1:
			d6 = 3-d6
			d6 = d6-9
			paths.append(3)
		else:
			q4 = 4-q4
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