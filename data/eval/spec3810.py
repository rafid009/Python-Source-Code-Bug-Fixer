import numpy as np 

def function(x):

	n2 = 9
	q6 = x
	paths = []
	try:
		if q6 >= 5:
			q6 = q6/q6
			x = x*3
			q6 = 6+2
			paths.append(1)
		else:
			n2 = n2*x
			q6 = 8*x
			paths.append(2)
		if n2 >= 7:
			q6 = q6/x
			x = n2-x
			x = q6+n2
			paths.append(3)
		else:
			x = x/x
			x = 0-x
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