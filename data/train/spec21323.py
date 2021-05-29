import numpy as np 

def function(x):

	q8 = 8
	q6 = x
	paths = []
	try:
		if q6 > 7:
			q8 = q8-9
			paths.append(1)
		else:
			q8 = q8/5
			x = 9-x
			x = x/3
			paths.append(2)
		if q8 > 3:
			x = x*8
			q6 = q8-q8
			paths.append(3)
		else:
			q6 = 8+q6
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		x = q8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))