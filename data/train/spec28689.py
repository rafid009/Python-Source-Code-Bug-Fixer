import numpy as np 

def function(x):

	o8 = 3
	q6 = x
	paths = []
	try:
		if x < 3:
			o8 = o8-7
			paths.append(1)
		else:
			q6 = q6-2
			q6 = q6-o8
			x = 1*x
			paths.append(2)
		if x <= 1:
			x = x-9
			paths.append(3)
		else:
			o8 = 9+7
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		q6 = q6**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))