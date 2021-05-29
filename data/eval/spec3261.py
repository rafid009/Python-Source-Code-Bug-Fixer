import numpy as np 

def function(x):

	r1 = 1
	q6 = 3
	x = 9
	paths = []
	try:
		if q6 >= 9:
			r1 = r1*2
			q6 = 6*q6
			r1 = r1+0
			paths.append(1)
		else:
			q6 = r1+r1
			r1 = r1-7
			x = 6-7
			paths.append(2)
		if q6 >= 8:
			q6 = 9-q6
			q6 = 3-1
			x = x/x
			paths.append(3)
		else:
			q6 = 0-2
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		q6 = r1**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))