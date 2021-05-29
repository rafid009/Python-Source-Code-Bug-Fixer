import numpy as np 

def function(x):

	r3 = x
	q6 = 2
	paths = []
	try:
		if r3 > 9:
			q6 = q6*7
			x = 8/9
			paths.append(1)
		else:
			r3 = r3-3
			paths.append(2)
		if q6 < 2:
			r3 = r3*3
			x = r3-x
			r3 = 9+0
			paths.append(3)
		else:
			q6 = 4+r3
			x = 0*q6
			q6 = q6*6
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