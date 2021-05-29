import numpy as np 

def function(x):

	x8 = x
	q9 = 3
	x = x
	paths = []
	try:
		if q9 > 4:
			x8 = x8*9
			x8 = x8*x8
			x = x8+x
			paths.append(1)
		else:
			x = x/5
			x = x8/2
			x8 = q9-x8
			paths.append(2)
		if q9 >= 2:
			q9 = q9/x
			q9 = 7+6
			x8 = x8/3
			paths.append(3)
		else:
			x8 = x8+6
			x8 = 7+0
			x = q9*x
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		q9 = x8**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))