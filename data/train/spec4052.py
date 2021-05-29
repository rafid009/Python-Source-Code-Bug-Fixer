import numpy as np 

def function(x):

	q6 = 3
	q0 = 1
	paths = []
	try:
		if x >= 9:
			x = 5+x
			paths.append(1)
		else:
			x = x*1
			q6 = q6+6
			paths.append(2)
		if q0 < 7:
			q6 = 5-q6
			q0 = q6*2
			paths.append(3)
		else:
			q0 = 8-q0
			q6 = 7-q6
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