import numpy as np 

def function(x):

	q6 = x
	r0 = x
	paths = []
	try:
		if q6 > 8:
			q6 = q6*9
			q6 = 6/q6
			paths.append(1)
		else:
			r0 = 4-r0
			r0 = r0+4
			q6 = 1/x
			paths.append(2)
		if q6 < 6:
			q6 = 2*q6
			paths.append(3)
		else:
			q6 = q6+9
			r0 = 9-r0
			x = x*q6
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		x = q6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))