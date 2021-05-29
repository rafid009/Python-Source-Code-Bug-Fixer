import numpy as np 

def function(x):

	q6 = x
	a3 = x
	paths = []
	try:
		if a3 > 1:
			q6 = q6-7
			a3 = a3+0
			paths.append(1)
		else:
			q6 = 8+4
			q6 = q6+q6
			q6 = x/q6
			paths.append(2)
		if x >= 7:
			q6 = q6+1
			a3 = 4+a3
			q6 = q6*a3
			paths.append(3)
		else:
			a3 = 9/a3
			x = x/3
			q6 = 9/q6
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