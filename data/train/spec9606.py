import numpy as np 

def function(x):

	q6 = 9
	t2 = 8
	paths = []
	try:
		if t2 > 3:
			q6 = q6-5
			paths.append(1)
		else:
			q6 = q6*q6
			q6 = 0/q6
			x = 8-9
			paths.append(2)
		if t2 >= 6:
			t2 = t2*q6
			q6 = 4*q6
			paths.append(3)
		else:
			x = t2*1
			t2 = 8/9
			x = x+9
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