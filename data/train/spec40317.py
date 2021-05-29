import numpy as np 

def function(x):

	d8 = x
	q8 = x
	paths = []
	try:
		if q8 < 5:
			x = 0-7
			paths.append(1)
		else:
			q8 = q8-5
			d8 = d8+x
			d8 = 7+1
			paths.append(2)
		if q8 >= 1:
			d8 = d8+2
			paths.append(3)
		else:
			d8 = 6*d8
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		d8 = q8**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))