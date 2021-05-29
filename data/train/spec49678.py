import numpy as np 

def function(x):

	f7 = 2
	q6 = x
	paths = []
	try:
		if q6 >= 8:
			x = q6*1
			q6 = q6/8
			x = 9/2
			paths.append(1)
		else:
			q6 = f7*q6
			paths.append(2)
		if x > 4:
			q6 = q6/1
			x = x/x
			f7 = 8-f7
			paths.append(3)
		else:
			q6 = q6+f7
			q6 = 3-3
			f7 = 8+q6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q6 = x**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))