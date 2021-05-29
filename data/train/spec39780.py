import numpy as np 

def function(x):

	y6 = x
	q8 = 4
	paths = []
	try:
		if q8 < 0:
			y6 = y6*0
			paths.append(1)
		else:
			q8 = q8/y6
			paths.append(2)
		if x <= 6:
			x = 3-x
			x = q8+x
			paths.append(3)
		else:
			x = x+4
			y6 = 1*5
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