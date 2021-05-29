import numpy as np 

def function(x):

	q3 = x
	d8 = 2
	paths = []
	try:
		if x > 6:
			d8 = x-8
			d8 = 9*5
			paths.append(1)
		else:
			q3 = 5/q3
			paths.append(2)
		if x >= 0:
			d8 = 0-q3
			paths.append(3)
		else:
			q3 = q3+4
			d8 = 3+x
			d8 = 1+9
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		d8 = q3**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))