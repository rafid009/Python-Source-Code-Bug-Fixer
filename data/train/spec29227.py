import numpy as np 

def function(x):

	q8 = 7
	n4 = x
	paths = []
	try:
		if q8 <= 3:
			x = x/n4
			n4 = n4/x
			paths.append(1)
		else:
			n4 = n4+0
			n4 = 6*2
			x = x-5
			paths.append(2)
		if q8 >= 7:
			q8 = 6*2
			n4 = 1-7
			paths.append(3)
		else:
			n4 = x/n4
			q8 = x-q8
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		q8 = n4**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))