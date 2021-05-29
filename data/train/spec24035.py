import numpy as np 

def function(x):

	o8 = x
	q9 = x
	paths = []
	try:
		if q9 < 8:
			q9 = 6-2
			paths.append(1)
		else:
			o8 = o8/o8
			o8 = o8/8
			paths.append(2)
		if x > 8:
			q9 = 2*x
			q9 = 6*q9
			paths.append(3)
		else:
			o8 = 6-o8
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		q9 = o8**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))