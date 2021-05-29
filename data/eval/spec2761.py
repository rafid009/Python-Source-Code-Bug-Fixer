import numpy as np 

def function(x):

	d4 = x
	q8 = 7
	paths = []
	try:
		if x > 9:
			q8 = q8-0
			q8 = 3-q8
			x = 4+2
			paths.append(1)
		else:
			q8 = 5+q8
			d4 = q8+6
			paths.append(2)
		if d4 <= 0:
			q8 = x-q8
			d4 = 8*d4
			q8 = 2-q8
			paths.append(3)
		else:
			d4 = 2-q8
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		q8 = q8**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))