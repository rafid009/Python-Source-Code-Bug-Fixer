import numpy as np 

def function(x):

	q8 = x
	a3 = 0
	x = 5
	paths = []
	try:
		if q8 >= 1:
			q8 = x/6
			paths.append(1)
		else:
			a3 = x+q8
			x = x/3
			paths.append(2)
		if x <= 0:
			x = x-3
			q8 = q8-x
			q8 = q8/5
			paths.append(3)
		else:
			a3 = q8*3
			x = 9/q8
			q8 = q8+0
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